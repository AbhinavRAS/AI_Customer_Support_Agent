import chromadb
from document_tool import chunks
from embedding import generate_embeddings

chunks = generate_embeddings(chunks)

client = chromadb.PersistentClient(
    path="./chroma_db"
)   

try:
    client.delete_collection("support_docs")
except:
    pass

collection = client.get_or_create_collection(
    name = "support_docs"
)

collection.add(
    ids = [f"chunk_{i}" for i, chunk in enumerate(chunks)],
    documents = [chunk["content"] for chunk in chunks],
    embeddings = [chunk["embedding"] for chunk in chunks],
    metadatas = [
        {
            "document": chunk["document"],
            "title" : chunk["title"]
        }
        for chunk in chunks
    ]
)
print(f"{collection.count()} chunks stored successfully")