# RAG-Chatbot-Basic

A basic Retrieval-Augmented Generation (RAG) chatbot project.

## Description

This project implements a simple RAG chatbot that retrieves information from a document and uses it to generate responses. It uses Python, with libraries like Langchain  and incorporate a vector database for efficient document retrieval.

## Setup

1.  **Create a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Linux/macOS
    .venv\Scripts\activate  # On Windows
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt 
    ```

3.  **Configure environment variables:**
    Create a `.env` file in the project root directory and set the necessary environment variables, such as API keys for LLMs . The project uses `.env` file, so these should be present in `.env` file
    

## Usage

1.  **Index documents:**
    Run the `index_documents.py` script to index the documents that the chatbot will use.
    ```bash
    python index_documents.py
    ```

2.  **Run the chatbot:**
    Execute the `rag_chatbot.py` script to start the chatbot.
    ```bash
    python rag_chatbot.py
    ```

## Files

*   `.env`:  Stores environment variables (API keys).
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
*   `index_documents.py`:  Script for indexing documents and creating vector embeddings.
*   `llm_utils.py`:  contains utility functions for interacting with the LLM.
*   `rag_chatbot.py`:  The main script for running the RAG chatbot.
*   `docker-compose.db.yml`: Docker configuration for running database

