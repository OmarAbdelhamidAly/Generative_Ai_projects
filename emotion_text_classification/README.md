<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>

<h1>Emotion Prediction Flask Application</h1>

<h2>Overview</h2>
<p>This Flask web application allows users to input text and receive emotion predictions based on the content of the text. The application uses a pretrained emotion classification model from the Hugging Face Transformers library to identify emotions such as sadness, joy, love, anger, fear, and surprise.</p>

<h2>Features</h2>
<ul>
    <li>Interactive web interface for text input.</li>
    <li>Utilizes a pretrained emotion classification model.</li>
    <li>Returns predicted emotions in JSON format.</li>
    <li>Error handling for empty or invalid inputs.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li><strong>Flask</strong>: A lightweight web framework for building the application.</li>
    <li><strong>Transformers</strong>: Hugging Face library for state-of-the-art natural language processing models.</li>
    <li><strong>TensorFlow</strong>: For running the emotion classification model.</li>
    <li><strong>NumPy</strong>: For handling numerical operations.</li>
</ul>

<h2>Setup Instructions</h2>
<ol>
    <li><strong>Clone the Repository:</strong>
        <pre><code>git clone https://github.com/YourUsername/Emotion-Prediction-Flask.git
cd Emotion-Prediction-Flask</code></pre>
    </li>
    <li><strong>Install Dependencies:</strong>
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Download or Prepare the Emotion Model:</strong>
        <p>Ensure that the emotion classification model is available and correctly referenced in your code. You may need to adjust the model path if necessary.</p>
    </li>
    <li><strong>Run the Application:</strong>
        <pre><code>python app.py</code></pre>
    </li>
    <li><strong>Access the Application:</strong>
        <p>Open your browser and navigate to <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a> to use the emotion prediction feature.</p>
    </li>
</ol>

<h2>How It Works</h2>
<ol>
    <li>The user enters text into the input form on the homepage.</li>
    <li>The text is sent to the <code>/predict</code> route for processing.</li>
    <li>The application uses the pretrained model to predict the emotion associated with the input text.</li>
    <li>The predicted emotion is returned as a JSON response.</li>
    <li>Any errors during processing are returned as error messages.</li>
</ol>

<h2>File Structure</h2>
<pre><code>
.
├── app.py                     # Main Flask application
├── requirements.txt           # Python dependencies
├── templates/
│   └── index.html             # HTML template for the input form
└── README.html                # Documentation (this file)
</code></pre>

<h2>Error Handling</h2>
<ul>
    <li><strong>Missing Input:</strong> The application will return an error message if the text input is empty.</li>
    <li><strong>Model Errors:</strong> Any issues related to the emotion model will be captured and returned as an error response.</li>
</ul>

<h2>Future Enhancements</h2>
<ul>
    <li><strong>Multi-Language Support:</strong> Add functionality to handle multiple languages for emotion prediction.</li>
    <li><strong>Sentiment Analysis:</strong> Extend the application to include sentiment analysis along with emotion prediction.</li>
    <li><strong>Detailed Reports:</strong> Provide detailed reports on emotion distribution over multiple inputs.</li>
</ul>

<h2>Contact</h2>
<ul>
    <li><strong>Author:</strong> Omar Abdelhamid</li>
    <li><strong>GitHub:</strong> <a href="https://github.com/OmarAbdelhamidAly">OmarAbdelhamidAly GitHub Profile</a></li>
    <li><strong>Email:</strong> <a href="mailto:omar.yaser.o.1322001@gmail.com">omar.yaser.o.1322001@gmail.com</a></li>
</ul>

</body>
</html>
