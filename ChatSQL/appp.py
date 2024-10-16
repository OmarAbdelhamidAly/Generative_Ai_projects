from flask import Flask, render_template, request, redirect, url_for, session
from pathlib import Path
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq
from langchain.agents.agent_toolkits import SQLDatabaseToolkit  # Make sure this import is here

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Route for the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db_option = request.form.get('db_option')
        api_key = request.form.get('api_key')
        
        if db_option == 'mysql':
            mysql_host = request.form.get('mysql_host')
            mysql_user = request.form.get('mysql_user')
            mysql_password = request.form.get('mysql_password')
            mysql_db = request.form.get('mysql_db')
            db_uri = "USE_MYSQL"
        else:
            db_uri = "USE_LOCALDB"
        
        session['api_key'] = api_key
        session['db_option'] = db_option
        session['db_uri'] = db_uri
        session['mysql_host'] = mysql_host if db_option == 'mysql' else None
        session['mysql_user'] = mysql_user if db_option == 'mysql' else None
        session['mysql_password'] = mysql_password if db_option == 'mysql' else None
        session['mysql_db'] = mysql_db if db_option == 'mysql' else None
        
        return redirect(url_for('chat'))
    
    return render_template('index.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if 'db_uri' not in session or 'api_key' not in session:
        return redirect(url_for('index'))

    db_uri = session['db_uri']
    api_key = session['api_key']
    mysql_host = session.get('mysql_host')
    mysql_user = session.get('mysql_user')
    mysql_password = session.get('mysql_password')
    mysql_db = session.get('mysql_db')

    # Initialize the LLM model
    try:
        llm = ChatGroq(groq_api_key=api_key, model_name="Llama3-8b-8192", streaming=True)
        print("LLM initialized successfully")
    except Exception as e:
        return f"Error initializing LLM: {e}"

    # Database configuration
    try:
        def configure_db(db_uri, mysql_host=None, mysql_user=None, mysql_password=None, mysql_db=None):
            if db_uri == "USE_LOCALDB":
                dbfilepath = (Path(__file__).parent / "student.db").absolute()
                creator = lambda: sqlite3.connect(f"file:{dbfilepath}?mode=ro", uri=True)
                return SQLDatabase(create_engine("sqlite:///", creator=creator))
            elif db_uri == "USE_MYSQL":
                if not (mysql_host and mysql_user and mysql_password and mysql_db):
                    return None
                return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"))

        db = configure_db(db_uri, mysql_host, mysql_user, mysql_password, mysql_db)
        if not db:
            return "Database connection failed. Please check your database credentials."
        
        print("Database configured successfully")
    except Exception as e:
        return f"Error configuring the database: {e}"

    # Initialize the SQLDatabaseToolkit
    try:
        toolkit = SQLDatabaseToolkit(db=db, llm=llm)
        agent = create_sql_agent(
            llm=llm,
            toolkit=toolkit,
            verbose=True,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
        )
        print("Agent initialized successfully")
    except Exception as e:
        return f"Error initializing agent: {e}"

    # Handle user input from the form
    if request.method == 'POST':
        user_query = request.form.get('user_query')
        if not user_query:
            return "Please enter a query to ask the database."
        
        print(f"User query: {user_query}")

        try:
            # Execute the query with the agent
            response = agent.run(user_query)
            print(f"Agent response: {response}")
            # Pass the response to the template
            return render_template('chat.html', query=user_query, response=response)
        except Exception as e:
            return f"Error running the agent: {e}"

    return render_template('chat.html')



# Run the app
if __name__ == '__main__':
    app.run(debug=True)
