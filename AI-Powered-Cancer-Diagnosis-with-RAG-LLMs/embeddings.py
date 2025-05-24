import os
from langchain_groq import ChatGroq
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import pickle  # For saving/loading embeddings
from langchain_community.document_loaders import PyPDFLoader


embeddings = OllamaEmbeddings()

def load_pdfs_from_directory(directory_path):
    docs = []
    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):  # Check if the file is a PDF
            filepath = os.path.join(directory_path, filename)
            loader = PyPDFLoader(filepath)  # Load each PDF file
            docs.extend(loader.load())  # Append to the list of documents
    return docs

# Replace with your actual folder path
directory_path = "research_papers"
documents = load_pdfs_from_directory(directory_path)

# Continue with text splitting and embeddings
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
final_documents = text_splitter.split_documents(documents[:50])  # Corrected to use 'documents'
vectors = FAISS.from_documents(final_documents, embeddings)

# Save the embeddings
with open("vectors.pkl", "wb") as file:
    pickle.dump(vectors, file)
