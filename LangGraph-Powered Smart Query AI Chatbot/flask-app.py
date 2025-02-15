# ✅ Import Required Libraries
import os
import uuid
from dotenv import load_dotenv
from typing import Annotated
from typing_extensions import TypedDict
from flask import Flask, render_template, request, jsonify, session
from langchain.schema import HumanMessage, AIMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langchain_community.utilities import arxiv
from langchain_community.tools import ArxivQueryRun
from langgraph.graph.message import add_messages
from langchain.schema import HumanMessage

# ✅ Load Environment Variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# ✅ Initialize LLM (ChatGroq)
llm = ChatGroq(groq_api_key=groq_api_key, model="mixtral-8x7b-32768", temperature=0)


# ✅ Initialize Tools (Arxiv Research)
arxiv_tool = ArxivQueryRun(api_wrapper=arxiv.ArxivAPIWrapper())
tools = [arxiv_tool]

# ✅ Define State for LangGraph
class State(TypedDict):
    messages: Annotated[list, add_messages]
    iteration_count: int  # Track iterations to prevent infinite loops

# ✅ Bind Tools to LLM
llm_with_tools = llm.bind_tools(tools=tools)

# ✅ Initialize LangGraph
graph_builder = StateGraph(State)
## 🔹 Add Chatbot Node
def chatbot(state:State):
  return {"messages":[llm_with_tools.invoke(state["messages"])]}

graph_builder.add_node("chatbot", chatbot)

## 🔹 Add Tool Execution Node (Handles External Queries)
tool_node = ToolNode(tools=tools)
graph_builder.add_node("tools", tool_node)
## 🔹 Sentiment Analyzer (LLM determines sentiment)
def sentiment_analyzer(data):
    """Uses LLM to analyze sentiment dynamically."""
    user_input = data["messages"][-1].content
    sentiment_analysis = llm.invoke(f"Analyze the sentiment of this message and classify it as 'positive', 'neutral', or 'negative': {user_input}")
    
    return {
        "sentiment": sentiment_analysis,
        "messages": [HumanMessage(content=f"Detected sentiment: {sentiment_analysis}")]
    }
    
graph_builder.add_node("sentiment_analyzer", sentiment_analyzer)


## 🔹 Memory Retrieval (LLM determines relevant context)
def memory_retriever(data):
    """Uses LLM to fetch relevant past interactions."""
    conversation_history = "Previously discussed topics: AI & ML"
    
    memory_response = llm.invoke(f"Given this history: '{conversation_history}', summarize what is most relevant for the user now.")
    
    return {
        "conversation_history": memory_response,
        "messages": [HumanMessage(content=f"Memory retrieved: {memory_response}")]
    }

graph_builder.add_node("memory_retriever", memory_retriever)


## 🔹 Query Expander (LLM refines user queries)
def query_expander(data):
    """LLM improves search queries to be more detailed and professional."""
    user_input = data["messages"][-1].content
    expanded_query = llm.invoke(f"Rewrite this search query to be more detailed and professional: {user_input}")
    
    return {
        "expanded_query": expanded_query,
        "messages": [HumanMessage(content=f"Searching for: {expanded_query}")]
    }

graph_builder.add_node("query_expander", query_expander)
## 🔹 Multi-Tool Execution (Runs multiple tools intelligently)
def multi_tool_executor(data):
    query = data.get("expanded_query", "default query")  # ✅ Prevents KeyError
    print(f"🔹 LLM Deciding Optimal Tools for: {query}")

    # Let the LLM decide which tools to use  
    tool_selection_prompt = f"Given the query '{query}', which tools should be executed? Available tools: {', '.join([tool.name for tool in tools])}."
    selected_tools = llm.invoke(tool_selection_prompt) # Expecting a comma-separated tool list

    results = {}
    for tool in tools:
        if tool.name in selected_tools:
            try:
                results[tool.name] = tool.run(query)
            except Exception as e:
                results[tool.name] = f"Tool failed: {e}"

    return {"tool_results": results, "messages": [HumanMessage(content="Fetched data from the best sources.")]}

graph_builder.add_node("multi_tool_executor", multi_tool_executor)


## 🔹 Verifier (LLM-Enhanced Validation)
def verifier(data):
    tool_results = data.get("tool_results", "No tool results available")

    # Let the LLM verify the correctness and reliability of tool outputs
    verification_prompt = f"Review the following data and validate its reliability:\n{tool_results}"
    verified_output = llm.invoke(verification_prompt)

    return {"verified_output": verified_output, "messages": [HumanMessage(content="Data verification completed by AI.")]}

graph_builder.add_node("verifier", verifier)


## 🔹 Conversation Logger (LLM-Assisted Logging)
def conversation_logger(data):
    """Stores interactions with structured tagging for analytics."""
    message_content = data["messages"][-1].content
    print(f"🔹 Logging conversation: {message_content}")

    # Let LLM structure logs with relevant metadata
    log_prompt = f"Generate a structured log entry for the message: {message_content}"
    structured_log = llm.invoke(log_prompt)

    return {"log_status": "Conversation stored", "messages": [HumanMessage(content=f"Log entry: {structured_log}")]}

graph_builder.add_node("conversation_logger", conversation_logger)


## 🔹 Feedback Handler (LLM-Driven Improvements)
def feedback_handler(data):
    """Processes user feedback and suggests AI improvements."""
    feedback = data["messages"][-1].content
    print(f"🔹 Processing feedback: {feedback}")

    # Let the LLM analyze feedback and suggest improvements
    feedback_analysis_prompt = f"Analyze this feedback and suggest AI improvements: {feedback}"
    improvement_suggestions = llm.invoke(feedback_analysis_prompt)

    return {
        "feedback_response": "Thanks for your feedback!",
        "messages": [HumanMessage(content=f"AI will improve based on your feedback: {improvement_suggestions}")]
    }

graph_builder.add_node("feedback_handler", feedback_handler)

## 🔹 Define Conditional Routing (Smart Decision-Making)
def chatbot_routing(data):
    """Routes user input based on detected intent & past memory."""
    
    user_input = data["messages"][-1].content.lower()
    sentiment = data.get("sentiment", "neutral")

    if "search" in user_input or "lookup" in user_input:
        return "query_expander"
    elif "analyze" in user_input or "process" in user_input:
        return "memory_retriever"
    elif "summarize" in user_input:
        return "multi_tool_executor"
    elif "verify" in user_input:
        return "verifier"
    elif "feedback" in user_input:
        return "feedback_handler"
    elif sentiment == "negative":
        return "conversation_logger"
    else:
        return "tools"

graph_builder.add_conditional_edges("chatbot", chatbot_routing)

## 🔹 Define Advanced Data Flow
graph_builder.add_edge("sentiment_analyzer", "chatbot")  # ✅ Sentiment influences AI's response
graph_builder.add_edge("memory_retriever", "chatbot")  # ✅ Retrieves past conversation data
graph_builder.add_edge("query_expander", "multi_tool_executor")  # ✅ Expands queries before search
graph_builder.add_edge("multi_tool_executor", "verifier")  # ✅ Validates tool-generated data
graph_builder.add_edge("verifier", "chatbot")  # ✅ Returns verified responses
graph_builder.add_edge("feedback_handler", "chatbot")  # ✅ Allows feedback-based improvements
graph_builder.add_edge("conversation_logger", "chatbot")  # ✅ Stores conversations for training
graph_builder.add_edge("tools", "chatbot")  # ✅ Standard tool-based response
graph_builder.add_edge(START, "chatbot")  # ✅ Start execution at chatbot

## 🔹 Compile the Graph
compiled_graph = graph_builder.compile()

# ───────────────────────────────────────────────
# 🔹 Flask Web Application
# ───────────────────────────────────────────────

# ✅ Initialize Flask App
app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/")
def home():
    """Renders the chatbot HTML page."""
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """Handles chatbot interaction requests."""
    user_input = request.json.get("message", "").strip()

    if not user_input:
        return jsonify({"response": "Please enter a valid message."})

    bot_response = chat_with_bot(user_input)

    return jsonify({"response": bot_response})

def chat_with_bot(user_input):
    """Processes user input through the chatbot graph."""

    max_iterations = 7  # ✅ Prevent looping by setting a limit
    final_keywords = ["Goodbye", "End of conversation", "Session ended", "Feedback received"]  # ✅ Stop on feedback

    # 🔹 Run LangGraph with user input
    events = compiled_graph.stream(
        {"messages": [HumanMessage(content=user_input)], "iteration_count": 0},  
        stream_mode="values"
    )

    iteration = 0
    bot_responses = []  # ✅ Store multiple responses if needed

    print("\n" + "=" * 50)  
    print("🧠 **Chatbot Conversation:**\n")

    for event in events:
        if "messages" in event:
            last_message = event["messages"][-1].content.strip()

            if not last_message:
                continue  # ✅ Skip empty responses  

            print(f"💡 **AI Response:** {last_message}\n")  
            bot_responses.append(last_message)

            # ✅ Stop if max iterations are reached
            iteration += 1
            if iteration >= max_iterations or any(phrase in last_message for phrase in final_keywords):
                print("✅ **Final response detected. Stopping execution.**")
                break  

    print("=" * 50)  

    # ✅ Combine all bot responses into a single full response
    full_response = " ".join(bot_responses) if bot_responses else "I'm not sure about that. Can you clarify?"

    return full_response  # ✅ Returns the complete response, not just the last message

if __name__ == "__main__":
    app.run(debug=True)




