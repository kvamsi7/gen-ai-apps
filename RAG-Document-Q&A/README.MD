# Documentation for RAG Document Q&A with Streamlit and Groq

## Overview
This script implements a Retrieval-Augmented Generation (RAG) pipeline using Streamlit, Groq LLM, FAISS for vector storage, and Hugging Face embeddings. The application loads research papers (PDFs), creates vector embeddings, and enables users to query documents using Groq's LLM.

## Dependencies
- `streamlit` for UI
- `langchain_groq`, `langchain_openai`, `langchain_community`, `langchain_huggingface` for LLM and embeddings
- `FAISS` for vector database
- `PyPDFDirectoryLoader` for loading PDFs
- `dotenv` for environment variables
- `os` and `time` for system operations

## Environment Variables
Ensure the following API keys are stored in a `.env` file:
- `OPENAI_API_KEY`
- `GROQ_API_KEY`
- `HF_TOKEN`

## Key Functionalities
### 1. **Loading Environment Variables**
```python
from dotenv import load_dotenv
load_dotenv()
```
Loads API keys from `.env`.

### 2. **Setting Up LLM and Embeddings**
```python
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
llm = ChatGroq(groq_api_key=groq_api_key, model_name="deepseek-r1-distill-llama-70b")
```
Uses `HuggingFaceEmbeddings` and `ChatGroq` for language processing.

### 3. **Creating Prompt Template**
```python
prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question

    <context>
    {context}
    <context>

    Question: {input}
    """
)
```
Defines a structured prompt to guide the LLM.

### 4. **Vector Embedding Creation**
```python
def create_vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = OpenAIEmbeddings()
        st.session_state.loader = PyPDFDirectoryLoader("data")
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:50])
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)
```
Loads PDFs, splits text, and stores vector embeddings in FAISS.

### 5. **Streamlit UI Setup**
```python
st.title('RAG Document Q&A Groq and Lama3')
user_prompt = st.text_input("Enter your query from the research paper")
```
Creates a UI for user interaction.

### 6. **Trigger Document Embedding**
```python
if st.button("Document Embedding"):
    create_vector_embedding()
    st.write("Vector Database is ready")
```
Allows users to process documents and build a vector database.

### 7. **Retrieval and Response Generation**
```python
if user_prompt:
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    response = retrieval_chain.invoke({'input': user_prompt})
    st.write(response['answer'])
```
Retrieves relevant document chunks and generates responses using Groq's LLM.

### 8. **Displaying Document Similarity Matches**
```python
with st.expander("Document similarity speech"):
    for i, doc in enumerate(response['context']):
        st.write(doc.page_content)
        st.write('------------------')
```
Displays retrieved documents for reference.

## Usage Instructions
1. Run the script using Streamlit:
   ```sh
   streamlit run app.py
   ```
2. Upload research papers into the `data/` directory.
3. Click "Document Embedding" to process documents.
4. Enter a query and receive an AI-generated response based on document retrieval.

## Potential Enhancements
- Add support for other embedding models.
- Implement caching to optimize document retrieval.
- Improve prompt engineering for better response quality.

