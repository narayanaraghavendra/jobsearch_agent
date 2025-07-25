def retrieve_top_k(query, index, docs, embedder, k=5):
    query_vec = embedder.encode([query])
    distances, indices = index.search(query_vec, k)
    return [docs[i] for i in indices[0]]