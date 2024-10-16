<h1>LangChain & ChatGroq Flask Application: Summarize YouTube and Website Content<h1>
Overview
<p>This project is a Flask-based web application that allows users to summarize content from a YouTube video or a webpage. It uses the <b>ChatGroq API</b> to generate high-quality summaries by leveraging the <b>LangChain</b> framework for prompt creation and document processing. The application takes a YouTube or website URL, loads the content, and returns a concise summary of around 300 words.</p>
Features
<ul> <li>Summarize content from <b>YouTube videos</b>.</li> <li>Summarize content from <b>webpages</b>.</li> <li>Supports different content loaders for web and video.</li> <li>Uses the <b>ChatGroq</b> model <b>Gemma-7b-It</b> to generate accurate and contextual summaries.</li> <li>User-friendly web interface with Flask.</li> </ul>
Technologies Used
<ul> <li><b>Flask</b>: For the web application framework, handling requests, and rendering the HTML templates.</li> <li><b>LangChain</b>: To manage LLM-based operations like loading documents and structuring prompts for summarization.</li> <li><b>ChatGroq</b>: For generating high-quality summaries using the <b>Gemma-7b-It</b> model.</li> <li><b>YoutubeLoader</b>: To extract content from YouTube videos.</li> <li><b>UnstructuredURLLoader</b>: To load and process text from a webpage.</li> <li><b>Validators</b>: For URL validation to ensure proper input handling.</li> </ul>
How It Works
<ol> <li><b>User Input:</b> The user provides the following inputs: <ul> <li><b>Groq API Key:</b> Required to connect to the ChatGroq service.</li> <li><b>URL:</b> Either a YouTube video link or a webpage URL to summarize.</li> </ul> </li> <li><b>Content Loading:</b> <ul> <li>If the URL is from YouTube, the app uses <b>YoutubeLoader</b> to extract and load the video’s content.</li> <li>For other URLs (webpages), <b>UnstructuredURLLoader</b> is used to extract text data from the page.</li> </ul> </li> <li><b>Summarization:</b> The extracted content is passed through the <b>Gemma-7b-It</b> model via ChatGroq API using a LangChain prompt. The prompt instructs the model to summarize the content in 300 words.</li> <li><b>Display Summary:</b> The generated summary is displayed on the same page below the form.</li> </ol>
Setup Instructions
<ol> <li><b>Clone the Repository:</b></li> <pre><code> git clone https://github.com/YourUsername/Flask-Summarizer.git cd Flask-Summarizer </code></pre> <li><b>Install Dependencies:</b></li> <pre><code> pip install -r requirements.txt </code></pre> <li><b>Configure the Application:</b> <p>Add your API key for <b>ChatGroq</b> when using the app.</p> </li> <li><b>Run the Application:</b></li> <pre><code> python app.py </code></pre> <li><b>Access the Application:</b> <p>Open your browser and go to <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a> to access the summarization tool.</p> </li> </ol>
Usage
<ol> <li>Go to the homepage at <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a>.</li> <li>Enter your <b>Groq API Key</b> and the URL of a YouTube video or webpage.</li> <li>Click <b>Submit</b>.</li> <li>The app will process the content, and within a few moments, display the summarized text below the form.</li> </ol>
File Structure
<pre><code> . ├── app.py # Main Flask application ├── templates/ │ └── index.html # HTML template for the web interface ├── static/ │ └── styles.css # (Optional) Custom styling for the app ├── requirements.txt # Python dependencies └── README.md # Documentation (this file) </code></pre>
Dependencies
<ul> <li><b>Flask</b></li> <li><b>LangChain</b></li> <li><b>ChatGroq</b></li> <li><b>YoutubeLoader</b></li> <li><b>UnstructuredURLLoader</b></li> <li><b>Validators</b></li> </ul>
All dependencies are listed in the <code>requirements.txt</code> file. Install them using <code>pip install -r requirements.txt</code>.

Error Handling
<ul> <li><b>Invalid URL:</b> The application will display an error message if the URL is invalid or does not correspond to a YouTube video or a webpage.</li> <li><b>Missing API Key:</b> If no Groq API key is provided, the app will prompt the user to input it.</li> <li><b>API Errors:</b> If the API request to ChatGroq fails (e.g., due to incorrect API key), an error message will be displayed on the screen.</li> </ul>
Future Enhancements
<ul> <li><b>Add More Model Options:</b> Allow users to select different models for summarization.</li> <li><b>Additional File Types:</b> Extend support to PDFs or other document types.</li> <li><b>Real-Time Summarization:</b> Provide real-time summarization with WebSockets for instant results.</li> </ul>
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
<ul> <li><b>Author:</b> [Your Name]</li> <li><b>Email:</b> [omar.yaser.o.1322001@gmail.com]</li> <li><b>GitHub:</b> <a href="https://github.com/OmarAbdelhamidAly/">Your GitHub Profile</a></li> </ul>
