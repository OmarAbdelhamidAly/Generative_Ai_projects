<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search Engine Application</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1, h2, h3, h4 {
            color: #007bff;
        }
        ul, ol {
            margin-left: 20px;
        }
        pre {
            background-color: #e9ecef;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
    </style>
</head>
<body>

<h1>Search Engine Application</h1>

<h2>Overview</h2>
<p>This project is a Flask-based web application that serves as a search engine for documents and information retrieval. It utilizes advanced NLP techniques and a retrieval model to allow users to query and find relevant documents efficiently. The application is designed to provide quick and accurate responses to user queries by leveraging a vector-based search mechanism.</p>

<h2>Features</h2>
<ul>
    <li>User-friendly web interface for inputting search queries.</li>
    <li>Utilizes a vector store for efficient document retrieval.</li>
    <li>Integrates with LangChain for handling language model operations.</li>
    <li>Supports various document formats and types for indexing.</li>
    <li>Provides relevant results based on user queries and context.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li><strong>Flask</strong>: For building the web application framework.</li>
    <li><strong>LangChain</strong>: To manage interactions with large language models and data processing.</li>
    <li><strong>Transformers</strong>: Hugging Face library for natural language processing tasks.</li>
    <li><strong>FAISS</strong>: For efficient similarity search and retrieval of documents.</li>
    <li><strong>TensorFlow</strong>: For handling deep learning operations.</li>
    <li><strong>NumPy</strong>: For numerical computations.</li>
</ul>

<h2>Setup Instructions</h2>
<ol>
    <li><strong>Clone the Repository:</strong>
        <pre><code>git clone https://github.com/OmarAbdelhamidAly/Generative_Ai_projects.git
cd Generative_Ai_projects/search_engine_app</code></pre>
    </li>
    <li><strong>Install Dependencies:</strong>
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Prepare Your Documents:</strong>
        <p>Ensure that the documents you want to index and search are available in the correct format.</p>
    </li>
    <li><strong>Run the Application:</strong>
        <pre><code>python app.py</code></pre>
    </li>
    <li><strong>Access the Application:</strong>
        <p>Open your browser and navigate to <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a> to use the search engine.</p>
    </li>
</ol>

<h2>How It Works</h2>
<ol>
    <li>The user enters a search query into the input form on the homepage.</li>
    <li>The application processes the query and retrieves relevant documents from the indexed dataset using vector similarity.</li>
    <li>Results are displayed to the user, providing links to the documents and snippets of relevant content.</li>
</ol>

<h2>File Structure</h2>
<pre><code>
.
├── app.py                     # Main Flask application for the search engine
├── requirements.txt           # Python dependencies
├── templates/
│   └── index.html             # HTML template for the search interface
├── static/
│   └── styles.css             # (Optional) Custom styling for the app
└── README.md                  # Documentation (this file)
</code></pre>

<h2>Error Handling</h2>
<ul>
    <li><strong>No Results Found:</strong> The application will inform the user if no results match their query.</li>
    <li><strong>Invalid Input:</strong> If the input query is empty or malformed, an error message will be displayed.</li>
</ul>

<h2>Future Enhancements</h2>
<ul>
    <li><strong>Advanced Filtering:</strong> Implement more advanced filtering options for search results.</li>
    <li><strong>Multi-Language Support:</strong> Extend the search engine to handle multiple languages for queries and documents.</li>
    <li><strong>Analytics Dashboard:</strong> Add an analytics dashboard to visualize user queries and search trends.</li>
</ul>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the LICENSE file for more details.</p>

<h2>Contact</h2>
<ul>
    <li><strong>Author:</strong> Omar Abdelhamid</li>
    <li><strong>Email:</strong> <a href="mailto:omar.yaser.o.1322001@gmail.com">omar.yaser.o.1322001@gmail.com</a></li>
    <li><strong>GitHub:</strong> <a href="https://github.com/OmarAbdelhamidAly/">Your GitHub Profile</a></li>
</ul>

</body>
</html>
