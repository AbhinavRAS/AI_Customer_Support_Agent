from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key = os.getenv("GROQ_API_KEY")
)

def generate_answer(question, context):
    """
    Generate an answer using the retrieved context.
    """

    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = [
            {
                "role" : "system",
                "content" : "You are an AI customer support assistant. Answer ONLY using the retrieved context. If the answer cannot be found in the context, reply: \"I don't know based on the provided information.\" Do not use outside knowledge."
            },
            {
                "role" : "user",
                "content" : f"""
                Context:
                {context}

                Question:
                {question}
                """
            }
        ],
        temperature = 0
    )
    return response.choices[0].message.content.strip()
