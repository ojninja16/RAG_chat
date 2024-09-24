import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

class RAGService:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings()
        self.vector_store = None
    def load_documents(self, pdf_dir):
        documents = []
        for filename in os.listdir(pdf_dir):
            if filename.endswith('.pdf'):
                loader = PyPDFLoader(os.path.join(pdf_dir, filename))
                documents.extend(loader.load())
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        texts = text_splitter.split_documents(documents)
        self.vector_store = FAISS.from_documents(texts, self.embeddings)
    def query(self, query: str, k: int = 4):
        if not self.vector_store:
            raise ValueError("Documents not loaded. Call load_documents first.")
        docs = self.vector_store.similarity_search(query, k=k)
        return [doc.page_content for doc in docs]

rag_service = RAGService()