from flask import Flask, render_template, request, session
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Necessary for Flask sessions

# Load environment variables
load_dotenv()

# Initialize API Wrappers
arxiv_wrapper = ArxivAPIWrapper(top_k_results=5, doc_content_chars_max=2000)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)
api_wrapper = WikipediaAPIWrapper(top_k_results=5, doc_content_chars_max=2000)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)
search = DuckDuckGoSearchRun(name="Search")

@app.route('/')
def index():
    # Initialize session for messages if not already initialized
    if 'messages' not in session:
        session['messages'] = [
            {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
        ]
    return render_template('index.html', messages=session['messages'])

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('user_input')
    api_key = request.form.get('api_key')

    # Append user input to messages
    session['messages'].append({"role": "user", "content": user_input})

    # LLM Configuration
    llm = ChatGroq(groq_api_key=api_key, model_name="Llama3-8b-8192", streaming=True)
    tools = [search, arxiv, wiki]

    # Extract the chat history (only user and assistant messages)
    chat_history = [
        {"role": message["role"], "content": message["content"]}
        for message in session['messages']
    ]

    # Initialize search agent
    search_agent = initialize_agent(
        tools, llm, agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION
    )

    # Run the search agent with user inputs and chat history
    response = search_agent.run({"input": user_input, "chat_history": chat_history})

    # Append assistant response to messages
    session['messages'].append({"role": "assistant", "content": response})

    return render_template('index.html', messages=session['messages'])

if __name__ == '__main__':
    app.run(debug=True)
