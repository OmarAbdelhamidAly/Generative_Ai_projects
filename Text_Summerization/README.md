<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
</head>
<body>

<h1>LangChain & ChatGroq Flask Application: Summarize YouTube and Website Content</h1>

<h2>Overview</h2>
<p>This project is a Flask-based web application that allows users to summarize content from a YouTube video or a webpage. It uses the <strong>ChatGroq API</strong> to generate high-quality summaries by leveraging the <strong>LangChain</strong> framework for prompt creation and document processing. The application takes a YouTube or website URL, loads the content, and returns a concise summary of around 300 words.</p>

<h2>Features</h2>
<ul>
    <li>Summarize content from <strong>YouTube videos</strong>.</li>
    <li>Summarize content from <strong>webpages</strong>.</li>
    <li>Supports different content loaders for web and video.</li>
    <li>Uses the <strong>ChatGroq</strong> model <strong>Gemma-7b-It</strong> to generate accurate and contextual summaries.</li>
    <li>User-friendly web interface with Flask.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li><strong>Flask</strong>: For the web application framework, handling requests, and rendering the HTML templates.</li>
    <li><strong>LangChain</strong>: To manage LLM-based operations like loading documents and structuring prompts for summarization.</li>
    <li><strong>ChatGroq</strong>: For generating high-quality summaries using the <strong>Gemma-7b-It</strong> model.</li>
    <li><strong>YoutubeLoader</strong>: To extract content from YouTube videos.</li>
    <li><strong>UnstructuredURLLoader</strong>: To load and process text from a webpage.</li>
    <li><strong>Validators</strong>: For URL validation to ensure proper input handling.</li>
</ul>

<h2>How It Works</h2>
<ol>
    <li><strong>User Input:</strong>
        <ul>
            <li><strong>Groq API Key:</strong> Required to connect to the ChatGroq service.</li>
            <li><strong>URL:</strong> Either a YouTube video link or a webpage URL to summarize.</li>
        </ul>
    </li>
    <li><strong>Content Loading:</strong>
        <ul>
            <li>If the URL is from YouTube, the app uses <strong>YoutubeLoader</strong> to extract and load the video’s content.</li>
            <li>For other URLs (webpages), <strong>UnstructuredURLLoader</strong> is used to extract text data from the page.</li>
        </ul>
    </li>
    <li><strong>Summarization:</strong> The extracted content is passed through the <strong>Gemma-7b-It</strong> model via ChatGroq API using a LangChain prompt. The prompt instructs the model to summarize the content in 300 words.</li>
    <li><strong>Display Summary:</strong> The generated summary is displayed on the same page below the form.</li>
</ol>

<h2>Setup Instructions</h2>
<ol>
    <li><strong>Clone the Repository:</strong>
        <pre><code>git clone https://github.com/YourUsername/Flask-Summarizer.git
cd Flask-Summarizer</code></pre>
    </li>
    <li><strong>Install Dependencies:</strong>
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Configure the Application:</strong>
        <p>Add your API key for <strong>ChatGroq</strong> when using the app.</p>
    </li>
    <li><strong>Run the Application:</strong>
        <pre><code>python app.py</code></pre>
    </li>
    <li><strong>Access the Application:</strong>
        <p>Open your browser and go to <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a> to access the summarization tool.</p>
    </li>
</ol>

<h2>Usage</h2>
<ol>
    <li>Go to the homepage at <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a>.</li>
    <li>Enter your <strong>Groq API Key</strong> and the URL of a YouTube video or webpage.</li>
    <li>Click <strong>Submit</strong>.</li>
    <li>The app will process the content, and within a few moments, display the summarized text below the form.</li>
</ol>

<h2>File Structure</h2>
<pre><code>
.
├── app.py                     # Main Flask application
├── templates/
│   └── index.html             # HTML template for the web interface
├── static/
│   └── styles.css             # (Optional) Custom styling for the app
├── requirements.txt           # Python dependencies
└── README.md                  # Documentation (this file)
</code></pre>

<h2>Dependencies</h2>
<ul>
    <li><strong>Flask</strong></li>
    <li><strong>LangChain</strong></li>
    <li><strong>ChatGroq</strong></li>
    <li><strong>YoutubeLoader</strong></li>
    <li><strong>UnstructuredURLLoader</strong></li>
    <li><strong>Validators</strong></li>
</ul>
<p>All dependencies are listed in the <code>requirements.txt</code> file. Install them using <code>pip install -r requirements.txt</code>.</p>

<h2>Error Handling</h2>
<ul>
    <li><strong>Invalid URL:</strong> The application will display an error message if the URL is invalid or does not correspond to a YouTube video or a webpage.</li>
    <li><strong>Missing API Key:</strong> If no Groq API key is provided, the app will prompt the user to input it.</li>
    <li><strong>API Errors:</strong> If the API request to ChatGroq fails (e.g., due to incorrect API key), an error message will be displayed on the screen.</li>
</ul>

<h2>Future Enhancements</h2>
<ul>
    <li><strong>Add More Model Options:</strong> Allow users to select different models for summarization.</li>
    <li><strong>Additional File Types:</strong> Extend support to PDFs or other document types.</li>
    <li><strong>Real-Time Summarization:</strong> Provide real-time summarization with WebSockets for instant results.</li>
</ul>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the LICENSE file for more details.</p>

<h2>Contact</h2>
<ul>
    <li><strong>Author:</strong> [Your Name]</li>
    <li><strong>Email:</strong> <a href="mailto:omar.yaser.o.1322001@gmail.com">omar.yaser.o.1322001@gmail.com</a></li>
    <li><strong>GitHub:</strong> <a href="https://github.com/OmarAbdelhamidAly/">Your GitHub Profile</a></li>
</ul>

</body>
</html>
