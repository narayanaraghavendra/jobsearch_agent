# 🔧 Job Recommendation WebApp (RAG-based)
# ---------------------------------------------------------------
# STACK: Python + Gradio + FAISS + SentenceTransformers + Gemini (or local LLM)
# FUNCTION: User enters skills or preferences -> relevant jobs shown (via RAG)
# ---------------------------------------------------------------

import gradio as gr
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# ✅ Load or simulate job data (ideally, replace with DB or CSV reader)
def load_jobs():
    with open("jobs_db.json", "r") as f:
        jobs = json.load(f)
    return jobs

# ✅ Embedder class
class EmbedStore:
    def __init__(self, documents, model="all-MiniLM-L6-v2"):
        if not documents:
            raise ValueError("Empty document list")
        self.docs = documents
        self.embedder = SentenceTransformer(model)
        self.embeddings = self.embedder.encode(documents, convert_to_numpy=True)
        self.index = self.build_index()

    def build_index(self):
        dim = self.embeddings.shape[1]
        index = faiss.IndexFlatL2(dim)
        index.add(self.embeddings)
        return index

    def retrieve(self, query, top_k=5):
        query_vec = self.embedder.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_vec, top_k)
        return [self.docs[i] for i in indices[0]]

def simple_generate(context, query):
    return f"\n\n Based on your input '{query}', here are some matching jobs:\n\n" + "\n\n".join(f"✅ {job}" for job in context)


def recommend_jobs(user_input):
    top_docs = store.retrieve(user_input, top_k=5)
    return simple_generate(top_docs, user_input)


jobs_data = load_jobs()
store = EmbedStore(jobs_data)


demo = gr.Interface(
    fn=recommend_jobs,
    inputs=gr.Textbox(placeholder="e.g. Python, React, Remote AI job in India"),
    outputs="text",
    title="Job Finder (AI-powered)",
    description="Enter your skill set or job preference and get instant matches using AI."
)

demo.launch()
