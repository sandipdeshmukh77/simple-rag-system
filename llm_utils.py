from openai import OpenAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
# Gemini-compatible OpenAI SDK
client = OpenAI(
     api_key=os.getenv('GOOGLE_API_KEY'),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def call_llm(query):
    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        messages=query
    )
    return response.choices[0].message.content

# Create embeddings
# Initialize Google Generative AI embeddings with the specified model
def initialize_embeddings():
    embeder = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    return embeder