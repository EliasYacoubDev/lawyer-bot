# Legal Chat Assistant

An interactive chatbot built with **Streamlit**, **LangChain**, and **OpenAI**, designed to assist with legal questions using Retrieval-Augmented Generation (RAG). The app supports multi-session chat, document-backed responses, and a user-friendly UI.

---

## Folder Structure

legal-chat-assistant/
│
├── app/
│ └── main.py # Streamlit UI and chat logic
│
├── rag_utils/
│ └── init.py # QA chain loader and RAG helper functions
│
├── data/
│ └── <your-docs>.pdf # Legal documents or datasets for context
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation



---

## Features

✅ **Multi-chat sessions**  
✅ **Named chat titles auto-generated from first question**  
✅ **Delete chats easily**  
✅ **LangChain QA chain with optional streaming**  
✅ **RAG-based legal question answering**  
✅ **Streamlit wide layout with sidebar**

---

## Getting Started

### 1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/legal-chat-assistant.git
cd legal-chat-assistant

### 2. Install Dependencies
pip install -r requirements.txt

Make sure you have an .env file (or set your environment variables manually) with your OpenAI API key:
OPENAI_API_KEY=your-api-key

### 3. Launch the App
streamlit run app/main.py
