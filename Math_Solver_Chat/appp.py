from flask import Flask, request, jsonify, render_template
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent

app = Flask(__name__)

# Initialize the LLM model
llm = None

def init_groq_model(api_key):
    global llm
    llm = ChatGroq(model="Gemma2-9b-It", groq_api_key=api_key)

# Initialize tools and chains
def setup_tools():
    wikipedia_wrapper = WikipediaAPIWrapper()
    wikipedia_tool = Tool(
        name="Wikipedia",
        func=wikipedia_wrapper.run,
        description="A tool for searching the Internet to find the various information on the topics mentioned"
    )

    # Math tool
    math_chain = LLMMathChain.from_llm(llm=llm)
    calculator_tool = Tool(
        name="Calculator",
        func=math_chain.run,
        description="A tool for answering math-related questions."
    )

    # Prompt for reasoning tool
    prompt = """
    You are an agent tasked with solving users' mathematical questions. Logically arrive at the solution and provide a detailed explanation,
    displaying it point-wise for the question below.
    Question: {question}
    Answer:
    """
    prompt_template = PromptTemplate(input_variables=["question"], template=prompt)
    chain = LLMChain(llm=llm, prompt=prompt_template)

    reasoning_tool = Tool(
        name="Reasoning Tool",
        func=chain.run,
        description="A tool for answering logic-based and reasoning questions."
    )

    return [wikipedia_tool, calculator_tool, reasoning_tool]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/solve', methods=['POST'])
def solve():
    data = request.get_json()
    groq_api_key = data.get('groq_api_key')
    question = data.get('question')

    if not groq_api_key:
        return jsonify({"error": "Please provide the Groq API key!"}), 400
    
    if not question:
        return jsonify({"error": "Please provide a question!"}), 400

    # Initialize the Groq model if not already initialized
    if not llm:
        init_groq_model(groq_api_key)

    # Setup tools and the agent
    tools = setup_tools()
    assistant_agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False,
        handle_parsing_errors=True
    )

    try:
        # Run the agent with the provided question
        response = assistant_agent.run(question)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
