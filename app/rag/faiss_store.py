from langchain_community.vectorstores import FAISS
from app.rag.embeddings import get_embeddings

class FAISSStore:
    def __init__(self):
        self.embeddings = get_embeddings()
        self.store = None
        print("Initialized FAISSStore with empty store.")
        print(f"Using embeddings: {self.embeddings}")

    def add_documents(self, docs):
        if self.store is None:
            self.store = FAISS.from_documents(docs, self.embeddings)
        else:
            self.store.add_documents(docs)

    def retriever(self):
        return self.store.as_retriever(search_kwargs={"k": 5})
