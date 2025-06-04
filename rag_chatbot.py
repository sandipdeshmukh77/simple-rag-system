from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from llm_utils import call_llm, initialize_embeddings
from dotenv import load_dotenv

# Set up embeddings and connect to existing vector store
embeder = initialize_embeddings()

retriver = QdrantVectorStore.from_existing_collection(
    embedding=embeder,
    collection_name="test_rag",
    url="http://localhost:6333"
)

# Chat loop
conversation_history = []

while True:
    query = input("Enter your question (or 'exit' to end): ")
    if query.lower() == 'exit':
        break

    relevant_chunks = retriver.similarity_search(query=query)

    # Define the system prompt for the chatbot
    system_prompt = f"""
    You are a helpful assistant. You help the user to find the answer to their question based on the provided context.
    context: {relevant_chunks}
    You will be provided with a context and a question. You need to answer the question based on the context.
    If the context does not provide enough information to answer the question, you should say "I don't know".
    Note:
    Answer should be in detaild and should not be too short.
    Answer should be in a conversational tone.
    """

    messages = [{"role": "system", "content": system_prompt}]

    # Add conversation history to messages
    for msg in conversation_history:
        messages.append(msg)

    # Add current user query to messages    
    messages.append({"role": "user", "content": query})

    response = call_llm(messages)

    conversation_history.append({"role": "user", "content": query})
    conversation_history.append({"role": "assistant", "content": response})

    # Keep conversation history limited to last 4 interactions (8 messages)
    if len(conversation_history) > 8:
        conversation_history = conversation_history[-8:]

    print("\nAssistant:", response, "\n")
