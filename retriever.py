from embedding import model
from llm import generate_answer
from vector_store import collection

def retrieve_answer(question):
    question_embedding = model.encode(question).tolist()

    result = collection.query(
        query_embeddings=[question_embedding],
        n_results=3,
        include=["documents", "metadatas"]
    )

    context = ""

    for document, metadata in zip(
        result["documents"][0],
        result["metadatas"][0]
    ):
        context += f"""Document: {metadata['document']}
        Title: {metadata['title']}
        {document}
        -----------------------------------------------
        """

    answer = generate_answer(question, context)
    return answer

if __name__ == "__main__":
    question = input("Ask a question: ")
    print("\n"+"="*60)
    print("AI Support Agent")
    print("="*60)
    print(retrieve_answer(question))