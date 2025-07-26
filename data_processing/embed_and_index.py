from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document
from data_processing.mongo_to_docs import load_case_summaries 

load_dotenv()

# — Load from MongoDB
raw_docs = load_case_summaries()

# — Convert to LangChain Document format
docs = [
    Document(page_content=doc["text"], metadata=doc["metadata"])
    for doc in raw_docs
]

# — Embed and store locally
embedding = OpenAIEmbeddings()
db = FAISS.from_documents(docs, embedding)
db.save_local("faiss_index")

print(f"✅ Indexed {len(docs)} documents and saved to faiss_index/")