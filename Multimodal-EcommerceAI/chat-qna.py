from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from peft import PeftModel
import pandas as pd

trained_tokenizer = AutoTokenizer.from_pretrained("tokenizer_Generative_qa_model")
base_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base").to("cuda")
base_model.resize_token_embeddings(len(trained_tokenizer))
trained_model = PeftModel.from_pretrained(base_model, "trainer_Generative_qa_model").to("cuda")

def generate_answer(question, context, model, tokenizer):
    input_text = f"question: {question} context: {context}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt").to("cuda")

    outputs = model.generate(
        input_ids=input_ids,
        max_length=128,
        min_length=20,
        num_beams=5,
        repetition_penalty=1.2,
        length_penalty=1.0,
        early_stopping=True
    )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer.strip()

def answer_natural_question(question, context=None, fallback_csv="single_qna.csv"):
    if context is None:
        df = pd.read_csv(fallback_csv)[['Question', 'Answer']].dropna().sample(1, random_state=42)
        context = df.iloc[0]['Answer']
    
    generated = generate_answer(question, context, trained_model, trained_tokenizer)

    return {
        "question": question,
        "used_context": context,
        "generated_answer": generated
    }

from transformers import AutoTokenizer, AutoModel
import torch.nn as nn

class DualEncoder(nn.Module):
    def __init__(self, model_name, output_dim=128):
        super().__init__()
        self.base_model = AutoModel.from_pretrained(model_name)
        self.projection = nn.Linear(self.base_model.config.hidden_size, output_dim)

    def forward(self, input_ids, attention_mask):
        output = self.base_model(input_ids=input_ids, attention_mask=attention_mask)
        cls_token = output.last_hidden_state[:, 0]
        return self.projection(cls_token)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name = 'sentence-transformers/all-MiniLM-L6-v2'
tokenizer = AutoTokenizer.from_pretrained(model_name)

question_encoder = DualEncoder(model_name).to(device)
answer_encoder = DualEncoder(model_name).to(device)
question_encoder.load_state_dict(torch.load("q_encoder_finetuned.pth", map_location=device))
answer_encoder.load_state_dict(torch.load("a_encoder_finetuned.pth", map_location=device))
question_encoder.eval()
answer_encoder.eval()

df = pd.read_csv("single_qna.csv")[['Question', 'Answer']].dropna()
df = df.sample(n=100000, random_state=42).reset_index(drop=True)
df.to_parquet("qna_df.parquet", index=False)

def get_embeddings(model, texts, batch_size=256):
    all_embeddings = []
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i+batch_size]
        tokens = tokenizer(batch_texts, padding=True, truncation=True, return_tensors='pt', max_length=64)
        tokens.pop("token_type_ids", None)
        tokens = {k: v.to(device) for k, v in tokens.items()}
        with torch.no_grad():
            emb = model(**tokens)
        all_embeddings.append(emb.cpu())
    return torch.cat(all_embeddings, dim=0)

embedding_path = "answer_embeddings.pt"
if not os.path.exists(embedding_path):
    print("➡️ Generating and saving answer embeddings...")
    answer_embeddings = get_embeddings(answer_encoder, df['Answer'].tolist())
    torch.save(answer_embeddings, embedding_path)
else:
    print("✅ Loading precomputed embeddings...")
    answer_embeddings = torch.load(embedding_path).to(device)

def get_top_k_answers_dual_encoder(question, top_k=3):
    q_emb = get_embeddings(question_encoder, [question]).to(device)  # <== move to same device
    sims = torch.matmul(q_emb, answer_embeddings.T).squeeze()
    topk_scores, topk_indices = torch.topk(sims, k=top_k)

    df = pd.read_parquet("qna_df.parquet")
    top_answers = []
    for score, idx in zip(topk_scores.tolist(), topk_indices.tolist()):
        top_answers.append({
            "answer": df.loc[idx, 'Answer'],
            "score": round(score, 4),
            "reference_question": df.loc[idx, 'Question']
        })

    return top_answers


from groq import Groq

groq_client = Groq(api_key=GROQ_API_KEY)

def improve_question_func(state: dict) -> dict:
    question = state["question"]
    response = groq_client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": f"Improve this e-commerce question: {question}"}]
    )
    improved = response.choices[0].message.content.strip()
    return {"improved_question": improved}

def retrieve_dual_encoder(state: dict) -> dict:
    improved_question = state["improved_question"]
    top_answers = get_top_k_answers_dual_encoder(improved_question, top_k=3)
    return {"dual_encoder_answers": top_answers}

def generate_final_answer(state: dict) -> dict:
    import re

    def sanitize_text(text: str) -> str:
        text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
        text = re.sub(r'[^\x20-\x7E]', '', text)
        return text.strip()

    question = state.get("question", "")
    dual_encoder_answers = state.get("dual_encoder_answers", [])

    examples_parts = []
    for ans in dual_encoder_answers:
        ref_q = sanitize_text(ans.get('reference_question', ''))
        ans_text = sanitize_text(ans.get('answer', ''))
        examples_parts.append(f"Q: {ref_q}\nA: {ans_text}")

    examples_section = "\n\n".join(examples_parts)

    print("==[ DEBUG: Similar QA examples (hint only) ]==")
    print(examples_section)

    fine_tuned_result = answer_natural_question(question, context="")
    fine_tuned_answer = fine_tuned_result.get('generated_answer', '')

    prompt = (
        "You are a knowledgeable and helpful assistant.\n\n"
        "Below are some Q&A pairs from similar questions. These are **not answers to the current question**, "
        "but they may help you understand the tone, style, or approach to take.\n\n"
        f"{examples_section}\n\n"
        f"The user asked:\n{sanitize_text(question)}\n\n"
        f"The initial answer was:\n{sanitize_text(fine_tuned_answer)}\n\n"
        "Please rewrite and improve the answer above, making it clearer, more helpful, and aligned with good examples."
    )

    messages = [
        {"role": "system", "content": "You are a helpful e-commerce assistant."},
        {"role": "user", "content": prompt}
    ]

    response = groq_client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages
    )

    grok_answer = response.choices[0].message.content.strip()

    return {"final_answer": grok_answer}

from typing import TypedDict, List, Dict, Any
from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda

class QAState(TypedDict):
    question: str
    improved_question: str
    dual_encoder_answers: List[Dict[str, Any]]
    final_answer: str

graph = StateGraph(state_schema=QAState)

graph.add_node("ImproveQuestion", RunnableLambda(improve_question_func))
graph.add_node("RetrieveDualEncoder", RunnableLambda(retrieve_dual_encoder))
graph.add_node("GenerateFinalAnswer", RunnableLambda(generate_final_answer))

graph.set_entry_point("ImproveQuestion")
graph.add_edge("ImproveQuestion", "RetrieveDualEncoder")
graph.add_edge("RetrieveDualEncoder", "GenerateFinalAnswer")
graph.add_edge("GenerateFinalAnswer", END)

qa_graph = graph.compile()

# === FLASK APP ===
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__, template_folder="templates")
CORS(app)

@app.route("/")
def serve_home():
    return render_template("ask.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        question = data.get("question", "").strip()

        if not question:
            return jsonify({"error": "Question is required"}), 400

        result = qa_graph.invoke({"question": question})
        return jsonify({
            "question": question,
            "answer": result.get("final_answer", "No answer generated.")
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

