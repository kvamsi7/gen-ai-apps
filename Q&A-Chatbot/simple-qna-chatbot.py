import os
from dotenv import load_dotenv

from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from the .env file
load_dotenv()

# Langsmith Tracking Configuration
# Set API key, tracing flag, and project name for Langsmith tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = os.getenv("LANGCHAIN_PROJECT")


# Define a prompt template for the chatbot
# The system message provides context for the assistant, and the user message includes a variable placeholder
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helful assistant, Please respond to the question asked clearly"),
        ("user","Question:{question}")
    ]
)

# Set up the Streamlit web app
st.title("Q&A Chatbot")# Title of the web app
input_text = st.text_input("Hit me your question!") # Input box for user to enter their query

# Initialize the Ollama LLM with the Llama2 model
llm = OllamaLLM(model = "llama2") # Specify the model to use
output_parser = StrOutputParser()
chain = prompt|llm|output_parser  # Combine the prompt, model, and output parser into a chain

# Handle user input and generate a response
if input_text:
    st.write(chain.invoke({'question':input_text}))
    