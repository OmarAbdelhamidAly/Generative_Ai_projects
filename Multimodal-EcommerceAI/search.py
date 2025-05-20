import os
import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from sentence_transformers import SentenceTransformer
import faiss

app = Flask(__name__)

# --- Helper function ---
def normalize(vectors):
    return vectors / np.linalg.norm(vectors, axis=1, keepdims=True)

# --- Load resources ---
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

# Load categories
index_dir = "faiss_indexes"
categories = sorted([
    f.split(".index")[0] for f in os.listdir(index_dir)
    if f.endswith(".index")
])

# Load all category indices and data
category_indices = {}
category_id_maps = {}

for category in categories:
    index_path = os.path.join(index_dir, f"{category}.index")
    data_path = os.path.join(index_dir, f"{category}_data.pkl")

    if os.path.exists(index_path) and os.path.exists(data_path):
        index = faiss.read_index(index_path)
        with open(data_path, "rb") as f:
            cat_df = pickle.load(f)

        category_indices[category] = index
        category_id_maps[category] = cat_df

# --- Recommendation Function ---
def get_recommendations(input_name, category, top_k=10):
    if category not in category_indices:
        return pd.DataFrame()

    input_embedding = model.encode([input_name])
    input_embedding = normalize(np.array(input_embedding).astype('float32'))

    index = category_indices[category]
    distances, indices = index.search(input_embedding, top_k)

    df_cat = category_id_maps[category]
    results = df_cat.iloc[indices[0]][['title', 'imgUrl', 'productURL']].copy()
    results['similarity'] = 1 - distances[0]
    return results.reset_index(drop=True)

# --- Routes ---
@app.route('/')
def home():
    return render_template('search.html', categories=categories)

@app.route('/recommend', methods=['POST'])
def recommend():
    query = request.form.get('query', '').strip()
    category = request.form.get('category', '')

    if not query or category not in categories:
        return render_template('search.html', categories=categories, error="Invalid input.")

    results = get_recommendations(query, category)

    if results.empty:
        return render_template('search.html', categories=categories, error="No results found.")

    return render_template('results.html', query=query, category=category, results=results)

# --- Run app ---
if __name__ == '__main__':
    app.run(debug=True)
