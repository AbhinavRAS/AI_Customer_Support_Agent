# AI Customer Support Agent using Retrieval-Augmented Generation (RAG)

## Overview

This project is an AI-powered Customer Support Agent that answers customer queries using Retrieval-Augmented Generation (RAG). It combines semantic search with a Large Language Model (Groq Llama) to generate accurate responses based only on the provided support documentation.

The application also supports order-related queries by retrieving customer order details directly from a structured CSV dataset. A routing mechanism automatically determines whether a user's query should be answered using structured order data or semantic document retrieval.

---

# Objectives

* Build an intelligent AI customer support assistant.
* Implement semantic document retrieval using embeddings.
* Generate context-aware responses using a Large Language Model.
* Support structured order lookups from CSV data.
* Demonstrate a complete Retrieval-Augmented Generation (RAG) pipeline.

---

# Features

* AI-powered customer support assistant
* Retrieval-Augmented Generation (RAG)
* Semantic search using Sentence Transformers
* ChromaDB vector database
* Groq Llama integration for answer generation
* CSV-based order lookup
* Automatic routing between order queries and policy queries
* Modular and scalable project structure

---

# Tech Stack

| Technology            | Purpose                   |
| --------------------- | ------------------------- |
| Python                | Programming Language      |
| Pandas                | CSV Order Data Processing |
| Sentence Transformers | Embedding Generation      |
| ChromaDB              | Vector Database           |
| Groq API              | Large Language Model      |
| python-dotenv         | Environment Variables     |
| Markdown              | Knowledge Base Documents  |

Embedding Model:

* all-MiniLM-L6-v2

LLM:

* Llama 3.3 70B Versatile (Groq)

---

# Project Structure

```text
support_agent/
│
├── sample_data/
│   ├── docs/
│   │   ├── account_and_support.md
│   │   ├── payment_and_pricing.md
│   │   ├── returns_and_refunds.md
│   │   └── shipping_policy.md
│   │
│   └── orders.csv
│
├── main.py
├── router.py
├── order_tool.py
├── document_tool.py
├── embedding.py
├── vector_store.py
├── retriever.py
├── llm.py
│
├── requirements.txt
├── README.md
└── .env
```

---

# Project Development Workflow

The project was developed incrementally by building each module independently before integrating them into a complete AI support system.

---

## Step 1: Order Lookup Module

A structured order lookup system was implemented using the provided CSV dataset.

Function:

* Reads order information from `orders.csv`
* Retrieves order details using the Order ID

Reason:

Order-related queries require structured data retrieval rather than an LLM.

Example:

```
Where is my order ORD1002?
```

---

## Step 2: Document Parsing

The customer support documents were stored as Markdown files.

These documents were parsed and divided into logical sections using Markdown headings.

Each chunk stores:

* Document Name
* Section Title
* Section Content

Reason:

Searching an entire document is inefficient. Splitting documents into semantic sections improves retrieval accuracy.

---

## Step 3: Embedding Generation

Each document chunk is converted into a dense vector representation using the Sentence Transformer model.

Model Used:

```
all-MiniLM-L6-v2
```

Each embedding is attached to its corresponding document chunk.

Reason:

Embeddings capture semantic meaning rather than keyword similarity, enabling semantic search.

---

## Step 4: Vector Database

The document chunks and their embeddings are stored in ChromaDB.

Stored Information:

* Chunk ID
* Document Content
* Embedding Vector
* Metadata

  * Document Name
  * Section Title

Reason:

ChromaDB enables efficient semantic similarity search.

---

## Step 5: Semantic Retrieval

When a user asks a question:

1. The question is converted into an embedding.
2. ChromaDB searches for the most similar document chunks.
3. The top matching chunks are retrieved.

Initially, retrieved chunks were printed for verification before integrating the LLM.

Reason:

Only the most relevant context should be provided to the language model.

---

## Step 6: LLM Integration

The retrieved document chunks are combined into a single context and passed to the Groq Llama model.

The system prompt instructs the LLM to:

* Answer only using the retrieved context.
* Avoid using external knowledge.
* Respond with "I don't know based on the provided information." if the answer is unavailable.

Reason:

This completes the Retrieval-Augmented Generation (RAG) pipeline while minimizing hallucinations.

---

## Step 7: Query Router

A routing mechanism was implemented using Regular Expressions.

If the query contains an Order ID:

```
ORD1002
```

The request is routed to the Order Lookup Module.

Otherwise:

The request is sent through the RAG pipeline.

Reason:

Different query types require different retrieval mechanisms.

---

## Step 8: Final Integration

All modules were integrated into a single AI application.

Workflow:

```
User Question
        │
        ▼
     main.py
        │
        ▼
     router.py
      /      \
     /        \
Order Tool   RAG Pipeline
                │
                ▼
          Sentence Transformer
                │
                ▼
             ChromaDB
                │
                ▼
             Retriever
                │
                ▼
             Groq LLM
                │
                ▼
          Final Response
```

---

# Architecture

```
                    User
                      │
                      ▼
                  main.py
                      │
                      ▼
                 router.py
                /         \
               /           \
              ▼             ▼
      order_tool.py    retriever.py
                             │
                             ▼
                      vector_store.py
                             │
                             ▼
                     SentenceTransformer
                             │
                             ▼
                         ChromaDB
                             │
                             ▼
                          llm.py
                             │
                             ▼
                    AI Generated Answer
```

---

# Challenges Faced

During development several issues were encountered and resolved.

### Challenge 1

Embeddings were generated but not stored with the document chunks.

Solution:

Each embedding was attached directly to its corresponding chunk before storing it in ChromaDB.

---

### Challenge 2

The vector store initially raised:

```
KeyError: 'embedding'
```

Solution:

Generated embeddings were stored inside each chunk dictionary before insertion into ChromaDB.

---

### Challenge 3

A circular import occurred between:

* main.py
* router.py

Solution:

The order lookup logic was moved into a separate `order_tool.py` module.

---

### Challenge 4

Initially, the retriever only printed document chunks.

Solution:

Groq Llama was integrated to generate natural language responses using the retrieved context.

---

# How It Works

1. User enters a question.
2. Router checks if the query contains an Order ID.
3. If an Order ID exists:

   * Retrieve order details from CSV.
4. Otherwise:

   * Convert the question into an embedding.
   * Retrieve relevant document chunks using ChromaDB.
   * Send retrieved context to Groq Llama.
   * Generate the final response.

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
cd support_agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

# Running the Project

```bash
python main.py
```

---

# Example Queries

### Order Query

```
Where is my order ORD1002?
```

---

### Shipping Query

```
How long does shipping take?
```

---

### Payment Query

```
Can I pay using UPI?
```

---

### Return Query

```
Can I return damaged products?
```

---

### Unknown Query

```
Who is the CEO of Microsoft?
```

Expected Output:

```
I don't know based on the provided information.
```

---

# Test Cases

| Test Case        | Input                        | Expected Output                                           | Status |
| ---------------- | ---------------------------- | --------------------------------------------------------- | ------ |
| Order Lookup     | Where is my order ORD1002?   | Returns order details                                     | ✅      |
| Shipping Policy  | How long does shipping take? | Returns shipping information                              | ✅      |
| Payment Method   | Can I pay using UPI?         | Returns accepted payment methods                          | ✅      |
| Unknown Question | Who is the CEO of Microsoft? | Returns "I don't know based on the provided information." | ✅      |

---

# Future Improvements

Given more development time, the following improvements could be implemented:

* Persistent ChromaDB without rebuilding the vector store on startup.
* Multi-turn conversational memory.
* Web interface using FastAPI or Streamlit.
* Integration with a real order management database.
* Metadata-based filtering during retrieval.
* Logging and monitoring.
* Authentication and user management.
* Evaluation metrics for retrieval quality and response accuracy.

---

# Author

**Abhinav Govardhana**

B.Tech Computer Science & Engineering (AI & ML)

Passionate about Artificial Intelligence, Large Language Models, Retrieval-Augmented Generation, and Full-Stack Development.
