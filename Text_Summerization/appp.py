from flask import Flask, render_template, request, flash
import validators
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Route for the home page
@app.route("/", methods=["GET", "POST"])
def index():
    summary = None
    if request.method == "POST":
        print("Form submitted, processing inputs...")  # Debugging statement
        groq_api_key = request.form.get("groq_api_key").strip()
        generic_url = request.form.get("generic_url").strip()

        # Validate form inputs
        if not groq_api_key or not generic_url:
            flash("Please provide both Groq API Key and URL.", "error")
            print("Missing API key or URL")  # Debugging statement
        elif not validators.url(generic_url):
            flash("Please provide a valid URL (either a YouTube video or website).", "error")
            print("Invalid URL")  # Debugging statement
        else:
            try:
                # Initialize the Groq API and LLM
                llm = ChatGroq(model="Gemma-7b-It", groq_api_key=groq_api_key)
                print("LLM initialized successfully")  # Debugging statement

                # Prompt Template for Summarization
                prompt_template = """
                Provide a summary of the following content in 300 words:
                Content: {text}
                """
                prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

                # Load content from the provided URL (YouTube or Website)
                if "youtube.com" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(generic_url, add_video_info=True)
                    print("Loading YouTube content")  # Debugging statement
                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify=False,
                        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
                    )
                    print("Loading website content")  # Debugging statement
                
                docs = loader.load()
                print(f"Loaded content: {docs}")  # Debugging statement

                # Chain for summarization
                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                summary = chain.run(docs)
                print("Summary generated")  # Debugging statement

                flash("Summarization successful!", "success")
            except Exception as e:
                flash(f"Error occurred: {e}", "error")
                print(f"Exception: {e}")  # Debugging statement

    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
