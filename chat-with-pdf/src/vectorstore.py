from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def create_vectorstore(documents, embeddings):
    vectorstore = Chroma.from_documents(documents=documents, embedding=embeddings)
    return vectorstore
