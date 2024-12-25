# Q&A Chatbot with Streamlit and LangChain

This project is a simple Q&A chatbot built using Streamlit, LangChain, and the Ollama LLM (`llama2`). It uses a modular approach with a custom prompt template to handle user queries and generate responses using the Llama2 model.

## Features

- Interactive chatbot interface using **Streamlit**.
- Custom prompt template to provide clear and helpful answers.
- Powered by **LangChain's Ollama LLM** (`llama2` model).
- Integrated with Langsmith for prompt tracking and debugging.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-name>


2. **Set Up a Virtual Environment (optional but recommended):**
    ```bash
    conda create -p venv python=3.10 -y
    activate venv/  


3. **Install Dependencies: Use the requirements.txt file (if available) or install the required libraries manually:**
    ```bash
    pip install streamlit langchain-ollama langchain-core python-dotenv

4. **Set Up Environment Variables:**
Create a .env file in the project directory.
Add the following environment variables

    ```bash
    LANGCHAIN_API_KEY=<your-langchain-api-key>
    LANGCHAIN_PROJECT=<your-project-name>
