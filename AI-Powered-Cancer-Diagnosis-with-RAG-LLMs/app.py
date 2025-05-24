from flask import Flask, request, render_template, jsonify
import os
from langchain_groq import ChatGroq
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_retrieval_chain, create_history_aware_retriever
from langchain_community.vectorstores import FAISS
from langchain_core.messages import AIMessage, HumanMessage
from dotenv import load_dotenv
import pickle  # For saving/loading embeddings

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if groq_api_key is None:
    raise ValueError("GROQ_API_KEY must be set in the .env file.")

# Initialize the ChatGroq model
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

# Cancer Doctor AI Prompt
system_prompt = """
You are an AI doctor specialized in cancer diagnosis and treatment, trained on a vast collection of research papers.
Your expertise includes lung, brain, chest, colon, and bone marrow cancers. Provide accurate and research-based answers.
Ensure that your response follows the latest medical guidelines.

<context>
{context}
<context>

Based on the context provided, offer a detailed and compassionate response to help the patient.
Include advice on treatment options, diagnosis, and follow-up care.

Question: {input}
"""

qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

# Contextualizing Question Prompt
contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question that can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed."
)

contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

# Load precomputed FAISS vectors
def load_precomputed_vectors():
    with open("vectors.pkl", "rb") as file:
        return pickle.load(file)

vectors = load_precomputed_vectors()  # Load embeddings on startup
retriever = vectors.as_retriever()

# Create history-aware retriever
history_aware_retriever = create_history_aware_retriever(llm, retriever, contextualize_q_prompt)

# Create document processing chain
question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

# RAG Chain
rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

# Initialize Flask app
app = Flask(__name__)
chat_history = []  # Stores conversation history

@app.route("/", methods=["GET", "POST"])
def index():
    global chat_history
    answer = None
    context = None

    if request.method == "POST":
        user_prompt = request.form.get("user_prompt")

        if vectors is None:
            answer = "The embedding database is not available."
        else:
            response = rag_chain.invoke({"input": user_prompt, "chat_history": chat_history})
            answer = response["answer"]

            # Update chat history
            chat_history.extend([
                HumanMessage(content=user_prompt),
                AIMessage(content=answer)
            ])

    return render_template("chatapp.html", answer=answer, history=chat_history)

if __name__ == "__main__":
    app.run(debug=True, port=5001, use_reloader=False)
