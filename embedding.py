from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
from document_tool import chunks

def generate_embeddings(chunks):
    for chunk in chunks:
        chunk["embedding"] = model.encode(chunk['content']).tolist()
    return chunks

chunks = generate_embeddings(chunks)
