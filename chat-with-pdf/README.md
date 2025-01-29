# Conversational Chat with PDFs

This application allows users to upload PDF documents, ask questions related to the content, and interact with the document's data using a retrieval-augmented generation (RAG) approach. The system leverages a combination of PDF document parsing, chat history management, and Groq LLM integration to provide context-aware responses to user queries.

## Features

- Upload multiple PDF files and parse their content.
- Generate embeddings using HuggingFace embeddings.
- Store and manage chat history for a conversational experience.
- Retrieve document-related information using a retrieval-augmented generation approach.
- Respond to user queries based on the uploaded document content and prior chat history.

## Requirements

Make sure you have the following installed:

- Python 3.7+
- Streamlit
- LangChain
- Groq API
- HuggingFace transformers
- Chroma (for vector database)
- PyPDFLoader (for PDF document loading)

To install the required packages, you can use the `requirements.txt` file.

## Setup

1. **Clone this repository or download the project files:**

    ```bash
    git clone <repository_url>
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Create a `.env` file to store your environment variables:**

    ```bash
    HF_TOKEN=<your_huggingface_token>
    ```

4. **Get your Groq API key:**  
   Obtain your API key from Groq and enter it in the input field of the app.

## Usage

### Running the Application

After setting up the environment, you can run the Streamlit app with the following command:

```bash
streamlit run app.py
```

## Uploading PDFs

- Upload PDFs using the file uploader provided in the Streamlit interface.
- The system will parse the documents and generate embeddings for efficient content retrieval.

## Asking Questions

- After uploading the PDFs, you can input your questions in the provided text box.
- The system will fetch relevant context from the uploaded documents and chat history to generate concise answers.

## Code Explanation

### Environment Setup

The application uses environment variables loaded from a `.env` file. The HuggingFace API token (`HF_TOKEN`) is required for generating embeddings.

### PDF Parsing

Uploaded PDF files are temporarily saved and parsed using the `PyPDFLoader`. After processing, the temporary files are deleted to free up space.

### Retrieval-Augmented Generation (RAG)

RAG is used to combine document retrieval and conversational history for question answering. This ensures that the assistant's answers are based on the latest context, which may include both uploaded documents and previous interactions.

### Chat History Management

Streamlit's session state is used to manage chat history. Each session maintains its own history, allowing for context-aware responses over multiple interactions.

## Notes

- Make sure to provide the **Groq API key** in the input box when prompted.
- Ensure the **HuggingFace token** is added to the `.env` file.
- Temporary PDF files are deleted after processing.

## Troubleshooting

- **Missing dependencies**: Ensure all required packages are installed by running `pip install -r requirements.txt`.
- **Groq API key issu

