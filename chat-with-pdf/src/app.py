import streamlit as st
from config import HF_TOKEN
from pdf_processing import process_pdf
from vectorstore import create_vectorstore
from retriever import create_history_aware_retriever_chain
from qa_chain import create_qa_chain
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
import chromadb.api
from langchain_core.runnables.history import RunnableWithMessageHistory

# to fix the tenant default_tenant issue 
chromadb.api.client.SharedSystemClient.clear_system_cache()
# Set up Streamlit UI
st.title("Conversational RAG with PDF uploads chat history")
st.write("Upload PDFs and chat with their content")

api_key = st.text_input("Enter your Groq API Key:", type="password")
session_id = st.text_input("Session ID", value="default_session")

# Initialize embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Check if Groq API key is provided
if api_key:
    llm = ChatGroq(groq_api_key=api_key, model_name="deepseek-r1-distill-llama-70b")

    # Stateful management of chat history
    if 'store' not in st.session_state:
        st.session_state.store = {}

    # PDF file upload and processing
    uploaded_files = st.file_uploader("Choose A PDF file", type="pdf", accept_multiple_files=True)
    if uploaded_files:
        documents = process_pdf(uploaded_files)

        # Create Chroma vectorstore
        vectorstore = create_vectorstore(documents, embeddings)
        retriever = vectorstore.as_retriever()

        # Create history-aware retriever
        history_aware_retriever = create_history_aware_retriever_chain(llm, retriever)

        # Create the question-answering chain
        rag_chain = create_qa_chain(llm, history_aware_retriever)

        # Function to get session history
        def get_session_history(session: str) -> BaseChatMessageHistory:
            if session not in st.session_state.store:
                st.session_state.store[session] = ChatMessageHistory()
            return st.session_state.store[session]


        conversational_rag_chain = RunnableWithMessageHistory(
            rag_chain, get_session_history,
            input_messages_key='input',
            history_messages_key="chat_history",
            output_messages_key="answer"
        )

        # Get session history
        session_history = get_session_history(session_id)

        # Conversational RAG chain
        user_input = st.text_input("Your question:")
        if user_input:
            response = conversational_rag_chain.invoke({"input": user_input}, config={"configurable": {"session_id": session_id}})
            st.write(st.session_state.store)
            st.write("Assistant: ", response['answer'])
            st.write("Chat History: ", session_history.messages)
else:
    st.warning("Please enter the GROQ API key")
