<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>

<h1>Flask Chatbot for Cancer Diagnosis</h1>

<h2>Overview</h2>
<p>This project is a Flask web application that provides a chatbot for cancer diagnosis and treatment inquiries. It utilizes the <strong>LangChain</strong> and <strong>ChatGroq</strong> frameworks to process user queries and generate responses based on a collection of cancer research papers.</p>

<h2>Features</h2>
<ul>
    <li>Interactive chatbot interface for cancer-related inquiries.</li>
    <li>Utilizes precomputed vector embeddings for context-aware responses.</li>
    <li>Integrates <strong>ChatGroq</strong> for generating natural language responses.</li>
    <li>Supports retrieval of contextual information based on user questions.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li><strong>Flask</strong>: A lightweight web framework for building the application.</li>
    <li><strong>LangChain</strong>: Framework for building applications powered by language models.</li>
    <li><strong>ChatGroq</strong>: API for utilizing large language models like <strong>Llama3-8b-8192</strong>.</li>
    <li><strong>Ollama Embeddings</strong>: For vector representations of text to improve response accuracy.</li>
    <li><strong>FAISS</strong>: For efficient similarity search and clustering of vectors.</li>
    <li><strong>dotenv</strong>: For managing environment variables, including sensitive keys.</li>
    <li><strong>pickle</strong>: For saving and loading embeddings from disk.</li>
</ul>

<h2>Setup Instructions</h2>
<ol>
    <li><strong>Clone the Repository:</strong>
        <pre><code>git clone https://github.com/YourUsername/Flask-Cancer-Chatbot.git
cd Flask-Cancer-Chatbot</code></pre>
    </li>
    <li><strong>Install Dependencies:</strong>
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Create a .env File:</strong>
        <p>Set your <strong>GROQ_API_KEY</strong> in a file named <code>.env</code>:</p>
        <pre><code>GROQ_API_KEY=your_api_key_here</code></pre>
    </li>
    <li><strong>Load Precomputed Vectors:</strong>
        <p>Ensure that you have a file named <code>vectors.pkl</code> containing precomputed embeddings.</p>
    </li>
    <li><strong>Run the Application:</strong>
        <pre><code>python app.py</code></pre>
    </li>
    <li><strong>Access the Application:</strong>
        <p>Open your browser and navigate to <a href="http://127.0.0.1:5001/">http://127.0.0.1:5001/</a> to interact with the chatbot.</p>
    </li>
</ol>

<h2>How It Works</h2>
<ol>
    <li><strong>User Input:</strong> The user enters a question related to cancer diagnosis or treatment.</li>
    <li><strong>Query Processing:</strong> The chatbot retrieves relevant context using the precomputed embeddings and processes the query.</li>
    <li><strong>Response Generation:</strong> The chatbot generates a compassionate and informative response based on the input and context.</li>
    <li><strong>Display Result:</strong> The response is presented back to the user in a conversational format.</li>
</ol>

<h2>File Structure</h2>
<pre><code>
.
├── app.py                     # Main Flask application
├── requirements.txt           # Python dependencies
├── templates/
│   ├── chatapp.html           # HTML template for the chatbot interface
│   ├── index.html             # Main HTML template
├── static/
│   └── styles.css             # (Optional) Custom styles for the application
├── vectors.pkl                # Precomputed embeddings
└── .env                       # Environment variables (including GROQ_API_KEY)
</code></pre>

<h2>Error Handling</h2>
<ul>
    <li><strong>Missing API Key:</strong> If the <code>GROQ_API_KEY</code> is not set, the application will raise a ValueError.</li>
    <li><strong>Embedding Database:</strong> The application will inform the user if the embedding database is unavailable.</li>
    <li><strong>API Errors:</strong> Any issues with the ChatGroq API will be reported to the user in the interface.</li>
</ul>

<h2>Future Enhancements</h2>
<ul>
    <li><strong>Enhanced NLP Capabilities:</strong> Improve the chatbot's natural language understanding for better response accuracy.</li>
    <li><strong>Multi-Language Support:</strong> Extend the chatbot's capabilities to handle inquiries in multiple languages.</li>
    <li><strong>Detailed Analytics:</strong> Add functionality for generating detailed reports based on user interactions.</li>
</ul>

<h2>Contact</h2>
<ul>
    <li><strong>Author:</strong> Omar Abdelhamid</li>
    <li><strong>GitHub:</strong> <a href="https://github.com/OmarAbdelhamidAly">OmarAbdelhamidAly GitHub Profile</a></li>
    <li><strong>Email:</strong> <a href="mailto:omar.yaser.o.1322001@gmail.com">omar.yaser.o.1322001@gmail.com</a></li>
</ul>

</body>
</html>
