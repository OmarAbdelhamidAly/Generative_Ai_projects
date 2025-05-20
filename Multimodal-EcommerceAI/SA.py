from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

app = Flask(__name__)

# ✅ Load model and tokenizer once when app starts
model = AutoModelForSequenceClassification.from_pretrained("sentiment-model")
tokenizer = AutoTokenizer.from_pretrained("sentiment-model")
model.eval()

# ✅ Prediction function
def predict_sentiment(texts):
    tokens = tokenizer(texts, truncation=True, padding=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**tokens)
        probs = torch.nn.functional.softmax(outputs.logits, dim=1)
        preds = torch.argmax(probs, dim=1)
    return preds.tolist(), probs.tolist()


from flask import render_template

@app.route('/')
def home():
    return render_template('SA.html')

# ✅ Flask route for inference
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    texts = data.get("texts", [])

    if not texts:
        return jsonify({"error": "No texts provided."}), 400

    preds, probs = predict_sentiment(texts)

    results = []
    for text, pred, prob in zip(texts, preds, probs):
        results.append({
            "text": text,
            "prediction": "positive" if pred == 1 else "negative",
            "class_id": int(pred),
            "probabilities": prob
        })

    return jsonify(results)

# ✅ Run the Flask app
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)

