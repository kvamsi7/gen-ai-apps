# Generative AI Applications

This repository contains a collection of Generative AI applications I've developed, showcasing my expertise in building interactive, scalable, and intelligent systems using state-of-the-art machine learning models and frameworks.

---

## Applications

### 1. **[Q&A Chatbot](https://github.com/kvamsi7/gen-ai-apps/tree/main/Q%26A-Chatbot)**
- **Description**: An interactive chatbot built with Streamlit and LangChain. This application uses the `llama2` model via Ollama LLM to answer user queries with clarity and accuracy. It integrates Langsmith for tracking and debugging prompts.
- **Key Features**:
  - User-friendly web interface for asking questions.
  - Customizable prompt templates for tailored responses.
  - Tracks and monitors prompt efficiency using Langsmith.

---

### 2. **[RAG Document Q&A](https://github.com/kvamsi7/gen-ai-apps/tree/main/RAG-Document-QA)**
- **Description**: A Retrieval-Augmented Generation (RAG) based Q&A system built with Streamlit and LangChain, utilizing FAISS for vector storage and document retrieval. This application answers user queries based on ingested research papers.
- **Key Features**:
  - Uses `ChatGroq` with the `deepseek-r1-distill-llama-70b` model for response generation.
  - Supports multiple embedding models including Hugging Face, OpenAI, and Ollama.
  - Ingests research papers using `PyPDFDirectoryLoader` and processes them with `RecursiveCharacterTextSplitter`.
  - Efficient document retrieval using FAISS vector database.
  - Real-time document similarity analysis and response generation.
  - Streamlit interface for easy interaction and document embedding.


### 3. **[Conversational chat with PDFs](https://github.com/kvamsi7/gen-ai-apps/tree/main/chat-with-pdf)**
- **Description**: A Retrieval-Augmented Generation (RAG) system for PDF documents and chat history. This application allows users to upload PDFs, ask questions related to their content, and interact with the document data using context-aware responses. It combines PDF parsing, chat history management, and Groq LLM integration.
- **Key Features**:
  - Uploads multiple PDF files and parses their content.
  - Generates embeddings using HuggingFace embeddings.
  - Stores and manages chat history for a conversational experience.
  - Retrieves document-related information using RAG approach for precise answers.
  - Streamlit interface for seamless interaction.
  - Real-time document similarity analysis and Q&A system using the Groq API.
  - Temporary PDF files are deleted after processing.

---
