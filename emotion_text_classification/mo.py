from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, TFAutoModel
import tensorflow as tf
import numpy as np

# # Define the Emotion Classifier
# class EmotionClassifier:
#     def __init__(self, model_dir, num_classes=6):
#         # Load BERT model and tokenizer
#         self.bert_model = TFAutoModel.from_pretrained(model_dir)
#         self.tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
#         self.num_classes = num_classes
#         self.classifier = self._build_classifier()

#     def _build_classifier(self):
#         # Create a classification layer on top of the loaded BERT model
#         input_ids = tf.keras.layers.Input(shape=(None,), dtype=tf.int32, name='input_ids')
#         attention_mask = tf.keras.layers.Input(shape=(None,), dtype=tf.int32, name='attention_mask')

#         # Get the pooled output from BERT
#         pooled_output = self.bert_model({'input_ids': input_ids, 'attention_mask': attention_mask})[1]
        
#         # Pass the pooled output to the Dense layer
#         output = tf.keras.layers.Dense(self.num_classes, activation='softmax')(pooled_output)

#         # Create the model
#         return tf.keras.Model(inputs={'input_ids': input_ids, 'attention_mask': attention_mask}, outputs=output)

#     def preprocess_text(self, text):
#         # Tokenize and preprocess the text
#         tokens = self.tokenizer(text, padding=True, truncation=True, return_tensors="tf")
#         return {
#             'input_ids': tokens['input_ids'],
#             'attention_mask': tokens['attention_mask']
#         }

#     def predict_emotion(self, text):
#         # Preprocess the text
#         inputs = self.preprocess_text(text)
        
#         # Perform prediction
#         predictions = self.classifier(inputs, training=False)

#         # Get the predicted class index
#         predicted_class = tf.argmax(predictions, axis=1).numpy()[0]

#         # Map class index to emotion label
#         emotion_labels = ['sadness', 'joy', 'love', 'anger', 'fear', 'surprise']
#         predicted_emotion = emotion_labels[predicted_class]

#         return predicted_emotion

from transformers import TFAutoModelForSequenceClassification, AutoTokenizer

loaded_model = TFAutoModelForSequenceClassification.from_pretrained('emotion_model')
loaded_tokenizer = AutoTokenizer.from_pretrained('emotion_model')

def predict_emotion(text):
    inputs = loaded_tokenizer(text, return_tensors='tf', truncation=True, padding=True)
    outputs = loaded_model(inputs)
    logits = outputs.logits  # Access logits directly
    predicted_class = tf.argmax(logits, axis=1).numpy()[0]
    emotion_labels = ['sadness', 'joy', 'love', 'anger', 'fear', 'surprise']
    return emotion_labels[predicted_class]

# Initialize the Flask app
app = Flask(__name__)

# Define the main route to render the HTML form
@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML template

# Define a prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.form  # Get the form data
    text = data.get("text")  # Extract the text from the input

    if not text:
        return jsonify({"error": "Please provide text input!"}), 400  # Return an error response

    try:
        print(f"Input Text: {text}")  # Debugging statement
        # Make prediction using the emotion classifier
        predicted_emotion = predict_emotion(text)

        # Return the predicted emotion
        return jsonify({"prediction": predicted_emotion})

    except Exception as e:
        print(f"Error: {str(e)}")  # Debugging statement
        return jsonify({"error": str(e)}), 500  # Return an error response if something goes wrong
# Run the app
if __name__ == '__main__':
    app.run(debug=True)
