from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from llm_utils import initialize_embeddings
from langchain_qdrant import QdrantVectorStore
from pathlib import Path
import os
from dotenv import load_dotenv

embeder = initialize_embeddings()
# Load your PDF
file_path = Path(__file__).parent / "nodejs.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
split_docs = text_splitter.split_documents(docs)

# Index into Qdrant
QdrantVectorStore.from_documents(
    documents=split_docs,
    embedding=embeder,
    collection_name="test_rag",
    url="http://localhost:6333"
)

print("Indexing completed successfully.")
