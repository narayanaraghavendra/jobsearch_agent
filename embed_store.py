from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from config import EMBED_MODEL

class EmbedStore:
    def __init__(self, documents):
        if not documents or not isinstance(documents, list):
            raise ValueError("No documents provided to EmbedStore or input is not a list of strings.")
        self.embedder = SentenceTransformer(EMBED_MODEL)
        self.docs = documents
        self.embeddings = self.embedder.encode(self.docs, convert_to_numpy=True)
        self.index = self.build_index()

    def build_index(self):
        if self.embeddings.ndim != 2:
            raise ValueError("Embeddings must be 2D. Check your input data.")
        dim = self.embeddings.shape[1]
        index = faiss.IndexFlatL2(dim)
        index.add(self.embeddings)
        return index

    def get_index(self):
        return self.index

    def get_docs(self):
        return self.docs

    def get_embedder(self):
        return self.embedder
