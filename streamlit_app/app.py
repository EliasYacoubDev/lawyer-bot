import streamlit as st
from rag_utils import load_qa_chain

st.set_page_config(page_title="Legal Chat Assistant", page_icon="⚖️", layout="wide")
st.title("⚖️ Legal Chat Assistant")


# Load chain (non-streaming for simplicity here)
@st.cache_resource
def get_qa_chain():
    return load_qa_chain(streaming=False)
qa_chain = get_qa_chain()

# Initialize session state
if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = []
    st.session_state.active_chat_id = None

# ─── Create New Chat ──────────────────────────────────────────────
def new_chat():
    new_id = len(st.session_state.chat_sessions)
    st.session_state.chat_sessions.append({"title": f"Chat {new_id + 1}", "messages": []})
    st.session_state.active_chat_id = new_id

# ─── Delete a Chat ────────────────────────────────────────────────
def delete_chat(index):
    st.session_state.chat_sessions.pop(index)
    if st.session_state.chat_sessions:
        st.session_state.active_chat_id = 0
    else:
        st.session_state.active_chat_id = None

# ─── Sidebar UI ───────────────────────────────────────────────────
st.sidebar.title("💬 Chats")
for i, chat in enumerate(st.session_state.chat_sessions):
    col1, col2 = st.sidebar.columns([0.75, 0.25])
    if col1.button(chat["title"], key=f"title_{i}"):
        st.session_state.active_chat_id = i
    if col2.button("🗑", key=f"delete_{i}"):
        delete_chat(i)
        st.rerun()

st.sidebar.button("➕ New Chat", on_click=new_chat)

# ─── Main Chat UI ─────────────────────────────────────────────────
if st.session_state.active_chat_id is not None:
    chat = st.session_state.chat_sessions[st.session_state.active_chat_id]

    if prompt := st.chat_input("Ask a legal question..."):
        # Add user message
        chat["messages"].append({"role": "user", "content": prompt})
        if len(chat["messages"]) == 1:
            chat["title"] = prompt[:30] + ("..." if len(prompt) > 30 else "")

        # Generate and display assistant response
        with st.chat_message("🤖"):
            with st.spinner("Thinking..."):
                response = qa_chain.invoke({"query": prompt})["result"]
                st.write(response)
                chat["messages"].append({"role": "assistant", "content": response})
            st.rerun()

    for msg in chat["messages"]:
        st.chat_message("🧑" if msg["role"] == "user" else "🤖").write(msg["content"])