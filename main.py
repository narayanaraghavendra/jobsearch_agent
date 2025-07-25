from fetch_jobs import fetch_jobs
from embed_store import EmbedStore
from retriever import retrieve_top_k
from generator import Generator
from config import TOP_K

def main():
    jobs = fetch_jobs()
    embed_store = EmbedStore(jobs)
    user_query = "Remote React developer jobs with 3+ years experience"
    top_docs = retrieve_top_k(
        query=user_query,
        index=embed_store.get_index(),
        docs=embed_store.get_docs(),
        embedder=embed_store.get_embedder(),
        k=TOP_K
    )
    generator = Generator()
    result = generator.generate("\n".join(top_docs), user_query)
    print("\n--- Recommended Jobs ---")
    print(result)

if __name__ == "__main__":
    main()