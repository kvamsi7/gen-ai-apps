from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def process_pdf(uploaded_files):
    documents = []
    for file in uploaded_files:
        temp_pdf_path = f"./temp_{file.name}.pdf"
        with open(temp_pdf_path, 'wb') as file_obj:
            file_obj.write(file.getvalue())
        
        loader = PyPDFLoader(temp_pdf_path)
        docs = loader.load()
        documents.extend(docs)
        
        # Delete the temporary PDF file after loading
        os.remove(temp_pdf_path)
        
    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=500)
    splits = text_splitter.split_documents(documents)
    return splits
