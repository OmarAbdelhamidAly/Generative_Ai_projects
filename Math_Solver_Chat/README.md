<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Math Problem Solver and Data Search Assistant</title>
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

<h1>Math Problem Solver and Data Search Assistant using ChatGroq and LangChain</h1>

<h2>Overview</h2>
<p>This project is a Flask-based web application that uses <strong>LangChain</strong> and <strong>ChatGroq</strong> to create an AI-powered assistant capable of solving mathematical problems, performing reasoning-based queries, and fetching data from Wikipedia. Users can interact with the system by submitting questions, and the assistant will provide detailed answers using the tools integrated into the application.</p>

<h2>Features</h2>
<ul>
    <li><strong>Mathematical Problem Solver</strong>: Solves mathematical expressions and provides detailed explanations using the ChatGroq LLM.</li>
    <li><strong>Reasoning and Logic-Based Question Solver</strong>: Handles questions requiring logic and reasoning.</li>
    <li><strong>Wikipedia Search</strong>: Retrieves relevant information from Wikipedia based on the user's query.</li>
    <li><strong>User-Friendly Interface</strong>: Provides an easy-to-use web interface for submitting questions and receiving responses.</li>
    <li><strong>API Support</strong>: Offers a REST API for external access to the assistant's functionalities.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li><strong>Flask</strong>: A lightweight web framework for building the application.</li>
    <li><strong>LangChain</strong>: For integrating tools and managing interactions with the language model (LLM).</li>
    <li><strong>ChatGroq</strong>: The language model used for solving mathematical and logic-based problems.</li>
    <li><strong>FAISS</strong>: (Optional) Can be used for similarity search.</li>
    <li><strong>WikipediaAPIWrapper</strong>: A utility for fetching data from Wikipedia.</li>
    <li><strong>HTML/CSS</strong>: For the front-end interface.</li>
</ul>

<h2>How It Works</h2>
<ol>
    <li><strong>User Input</strong>: The user enters a <strong>Groq API key</strong> and submits a <strong>math problem</strong> or <strong>data-related question</strong> (e.g., asking Wikipedia).</li>
    <li><strong>Tool Selection</strong>: The system uses <strong>LangChain</strong> to select the appropriate tool (math solver, reasoning, or Wikipedia search) based on the user's query.</li>
    <li><strong>LLM Interaction</strong>: The <strong>ChatGroq</strong> model processes the question and generates a detailed response.</li>
    <li><strong>Result Display</strong>: The result is displayed back to the user on the same page in a user-friendly format.</li>
</ol>

<h2>Setup Instructions</h2>
<ol>
    <li><strong>Clone the Repository:</strong>
        <pre><code>git clone https://github.com/YourUsername/Math-Problem-Solver-Assistant.git
cd Math-Problem-Solver-Assistant</code></pre>
    </li>
    <li><strong>Install Dependencies:</strong> Make sure you have Python installed, then install the required packages by running:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Add Your API Key:</strong> You'll need a <strong>Groq API key</strong> to access the language model. Create a <code>.env</code> file in the root of the project and add your API key:
        <pre><code>GROQ_API_KEY=your_api_key_here</code></pre>
    </li>
    <li><strong>Run the Flask Application:</strong> Start the Flask application by running the following command:
        <pre><code>python app.py</code></pre>
    </li>
    <li><strong>Access the Application:</strong> The application will start at <code>http://127.0.0.1:5000/</code>.
    </li>
</ol>

<h2>Usage</h2>
<ol>
    <li>Open your browser and navigate to <code>http://127.0.0.1:5000/</code>.</li>
    <li>Enter your <strong>Groq API Key</strong> in the form.</li>
    <li>Type in a mathematical problem or data-related query (such as "How many planets are there in the solar system?").</li>
    <li>Press <strong>Submit</strong> and wait for the response to appear on the screen.</li>
</ol>

<h2>API Usage</h2>
<p>You can also interact with the assistant via the API. Make a POST request to <code>http://127.0.0.1:5000/api/solve</code> with the following JSON payload:</p>
<pre><code>{
  "groq_api_key": "your_api_key",
  "question": "Enter your math problem or question here"
}</code></pre>

<p>The response will contain the solution or relevant information:</p>
<pre><code>{
  "response": "Your answer will appear here."
}</code></pre>

<h2>File Structure</h2>
<pre><code>.
├── app.py                     # Main Flask application
├── templates/
│   └── index.html             # HTML template for the web interface
├── static/
│   └── styles.css             # (Optional) Custom styles for the app
├── requirements.txt           # Python dependencies
└── README.md                  # Documentation
</code></pre>

<h2>Error Handling</h2>
<ul>
    <li><strong>Invalid API Key</strong>: If no Groq API key is provided or the key is incorrect, the app will display an error message.</li>
    <li><strong>Invalid Input</strong>: If the question field is empty or invalid, the app will prompt the user to provide input.</li>
    <li><strong>API Errors</strong>: In case of API errors from Groq, the error will be displayed on the screen.</li>
</ul>

<h2>Future Enhancements</h2>
<ul>
    <li><strong>Add More Tools</strong>: Integrate more tools for other types of questions (e.g., scientific or historical queries).</li>
    <li><strong>Real-Time Updates</strong>: Implement real-time interaction using WebSockets for quicker response times.</li>
    <li><strong>Enhance UI</strong>: Add more design features and usability improvements to the web interface.</li>
</ul>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

<h2>Contact</h2>
<ul>
    <li><strong>Author</strong>: [Your Name]</li>
    <li><strong>Email</strong>: <a href="mailto:your-email@example.com">your-email@example.com</a></li>
    <li><strong>GitHub</strong>: <a href="https://github.com/YourUsername">Your GitHub Profile</a></li>
</ul>

</body>
</html>
