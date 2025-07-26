import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_core.callbacks import CallbackManager

def load_qa_chain(
    faiss_dir="faiss_index",
    model_name="gpt-4o",
    temperature=0,
    k=4,
    streaming=True
):
    load_dotenv()
    openai_key = os.getenv("OPENAI_API_KEY")

    # Setup callback manager
    callback_handler = StreamingStdOutCallbackHandler()
    callback_manager = CallbackManager([callback_handler]) if streaming else None

    # Load FAISS vector store
    embedding_model = OpenAIEmbeddings(openai_api_key=openai_key)
    vectorstore = FAISS.load_local(faiss_dir, embedding_model, allow_dangerous_deserialization=True)

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )

    llm = ChatOpenAI(
        model=model_name,
        openai_api_key=openai_key,
        temperature=temperature,
        streaming=streaming,
        callbacks=[callback_handler] if streaming else None
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )
    return qa_chain
