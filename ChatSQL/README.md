<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    

</head>
<body>

<h1>Flask SQL Chatbot Application</h1>

<h2>Overview</h2>
<p>This project is a Flask web application that allows users to interact with a SQL database using natural language. It utilizes <strong>LangChain</strong> and <strong>ChatGroq</strong> to create a chatbot interface that processes user queries, translates them into SQL commands, and returns results from the database. Users can choose between connecting to a local SQLite database or a MySQL database.</p>

<h2>Features</h2>
<ul>
    <li>Interactive chatbot interface for querying a SQL database.</li>
    <li>Supports both <strong>SQLite</strong> and <strong>MySQL</strong> databases.</li>
    <li>Uses <strong>LangChain</strong> for managing the language model and SQL integration.</li>
    <li>Utilizes <strong>ChatGroq</strong> to process natural language input and generate SQL queries.</li>
    <li>User session management for handling database connections securely.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li><strong>Flask</strong>: A lightweight web framework for building the application.</li>
    <li><strong>LangChain</strong>: Framework for working with large language models (LLMs) to create agent-based applications.</li>
    <li><strong>ChatGroq</strong>: API for utilizing powerful language models like <strong>Llama3-8b-8192</strong>.</li>
    <li><strong>SQLAlchemy</strong>: Toolkit for SQL database interactions and ORM support.</li>
    <li><strong>SQLite</strong>: Lightweight database engine used for local storage.</li>
    <li><strong>MySQL</strong>: Database system for handling more extensive data needs.</li>
</ul>

<h2>Setup Instructions</h2>
<ol>
    <li><strong>Clone the Repository:</strong>
        <pre><code>git clone https://github.com/OmarAbdelhamidAly/Flask-SQL-Chatbot.git
cd Flask-SQL-Chatbot</code></pre>
    </li>
    <li><strong>Install Dependencies:</strong>
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Configure Database:</strong>
        <p>Ensure you have either a local SQLite database named <code>student.db</code> in the project directory or access to a MySQL database. If using MySQL, prepare the connection details: host, user, password, and database name.</p>
    </li>
    <li><strong>Run the Application:</strong>
        <pre><code>python app.py</code></pre>
    </li>
    <li><strong>Access the Application:</strong>
        <p>Open your browser and go to <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a> to interact with the chatbot.</p>
    </li>
</ol>

<h2>How It Works</h2>
<ol>
    <li><strong>User Input:</strong> The user selects the database option (MySQL or SQLite) and enters their API key and database credentials.</li>
    <li><strong>Session Management:</strong> The application manages user sessions to maintain state across requests.</li>
    <li><strong>Chatbot Interaction:</strong> Users can input natural language queries into the chatbot, which processes the input and generates SQL queries based on the context.</li>
    <li><strong>Database Queries:</strong> The application connects to the selected database and executes the generated SQL queries, returning the results to the user in a conversational format.</li>
</ol>

<h2>File Structure</h2>
<pre><code>
.
├── app.py                     # Main Flask application
├── requirements.txt           # Python dependencies
├── templates/
│   ├── index.html             # Main HTML template
│   ├── chat.html              # Chat interface template
├── static/
│   └── styles.css             # (Optional) Custom styles for the application
└── README.md                  # Documentation (this file)
</code></pre>

<h2>Error Handling</h2>
<ul>
    <li><strong>Invalid Credentials:</strong> If database credentials are incorrect, the application will prompt the user to check their input.</li>
    <li><strong>API Errors:</strong> If there is an issue with the ChatGroq API request, an error message will be displayed.</li>
    <li><strong>SQL Errors:</strong> Any SQL execution errors will be caught and presented to the user.</li>
</ul>

<h2>Future Enhancements</h2>
<ul>
    <li><strong>Natural Language Understanding:</strong> Improve the chatbot's understanding of complex queries.</li>
    <li><strong>Multi-Language Support:</strong> Extend support for querying in multiple languages.</li>
    <li><strong>Advanced Analytics:</strong> Implement features for more advanced analytics and reporting directly from the chatbot.</li>
</ul>

<h2>Contact</h2>
<ul>
    <li><strong>Author:</strong> Omar Abdelhamid</li>
    <li><strong>GitHub:</strong> <a href="https://github.com/OmarAbdelhamidAly">OmarAbdelhamidAly GitHub Profile</a></li>
    <li><strong>Email:</strong> <a href="mailto:omar.yaser.o.1322001@gmail.com">omar.yaser.o.1322001@gmail.com</a></li>
</ul>

</body>
</html>
