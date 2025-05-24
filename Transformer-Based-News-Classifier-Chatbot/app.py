from flask import Flask, request, jsonify, render_template
import torch
import json
import numpy as np
import os
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# ✅ Initialize Flask App
app = Flask(__name__)

# ✅ Load Model Configuration
model_path = "model"
with open(f"{model_path}/config.json", "r") as f:
    config = json.load(f)

# ✅ Load Tokenizer & BERT Model
tokenizer = BertTokenizer.from_pretrained(model_path)
embedding_model = BertModel.from_pretrained("bert-base-uncased").to("cuda" if torch.cuda.is_available() else "cpu")

# ✅ Define TransformerClassifier Model
class TransformerClassifier(torch.nn.Module):
    def __init__(self, input_dim, num_classes, num_heads, hidden_dim, num_layers, dropout):
        super(TransformerClassifier, self).__init__()
        self.transformer = torch.nn.TransformerEncoder(
            torch.nn.TransformerEncoderLayer(d_model=input_dim, nhead=num_heads, dim_feedforward=hidden_dim, dropout=dropout, batch_first=True),
            num_layers=num_layers
        )
        self.fc = torch.nn.Linear(input_dim, num_classes)
        self.dropout = torch.nn.Dropout(dropout)

    def forward(self, x):
        x = self.transformer(x)
        x = x.mean(dim=1)
        x = self.dropout(x)
        x = self.fc(x)
        return x

# ✅ Load Model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = TransformerClassifier(**config).to(device)
model.load_state_dict(torch.load(f"{model_path}/model.pth", map_location=device))
model.eval()

# ✅ Define Category Labels
category_labels = {0: 'U.S. NEWS', 1: 'COMEDY', 2: 'PARENTING', 3: 'WORLD NEWS', 4: 'CULTURE & ARTS',
    5: 'TECH', 6: 'SPORTS', 7: 'ENTERTAINMENT', 8: 'POLITICS', 9: 'WEIRD NEWS',
    10: 'ENVIRONMENT', 11: 'EDUCATION', 12: 'CRIME', 13: 'SCIENCE', 14: 'WELLNESS',
    15: 'BUSINESS', 16: 'STYLE & BEAUTY', 17: 'FOOD & DRINK', 18: 'MEDIA',
    19: 'QUEER VOICES', 20: 'HOME & LIVING', 21: 'WOMEN'}

# ✅ Function to Predict Category
def predict_category(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    inputs = {key: value.to(device) for key, value in inputs.items()}
    with torch.no_grad():
        embeddings = embedding_model(**inputs).last_hidden_state.mean(dim=1).unsqueeze(0)
        outputs = model(embeddings)
        predicted_class = torch.argmax(outputs, dim=1).item()
    return category_labels[predicted_class]

# ✅ Load News Data
with open("filtered_news.json", "r", encoding="utf-8") as f:
    news_data = json.load(f)

# ✅ Function to Compute Sentence Embeddings
def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding="max_length", max_length=128)
    inputs = {key: value.to(device) for key, value in inputs.items()}
    with torch.no_grad():
        embedding = embedding_model(**inputs).last_hidden_state.mean(dim=1).cpu().numpy()
    return embedding

# ✅ Function to Find Similar Articles
def get_similar_articles(text, predicted_category, top_n=10):
    category_articles = [article for article in news_data if article["category"] == predicted_category]
    if not category_articles:
        return []
    input_embedding = get_embedding(text)
    article_embeddings = np.vstack([get_embedding(article["headline"]) for article in category_articles])
    similarities = cosine_similarity(input_embedding, article_embeddings).flatten()
    top_indices = similarities.argsort()[-top_n:][::-1]
    return [category_articles[i] for i in top_indices]

# ✅ Load API Key & Initialize LLM
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

# ✅ Function to Get Response
def get_response(user_query):
    predicted_category = predict_category(user_query)
    similar_articles = get_similar_articles(user_query, predicted_category, top_n=10)
    response = llm.invoke(f"User Query: {user_query}\nPredicted Category: {predicted_category}\n\nGenerate a helpful response based on the category.")
    return response, predicted_category, similar_articles

# ✅ Flask Routes
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["text_input"]
        if text:
            response, category, articles = get_response(text)
            return render_template("index.html", text=text, category=category, response=response, articles=articles)
    return render_template("index.html", text=None, category=None, response=None, articles=None)

# ✅ Run Flask App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
