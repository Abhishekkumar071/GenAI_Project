import streamlit as st
from backend import handle_query

st.set_page_config(page_title="AI Tutor", layout="wide")

st.title("🤖 AI Tutor + PDF Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
user_input = st.chat_input("Ask something...")

if user_input:

    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response
    with st.spinner("Thinking..."):
        response, agent = handle_query(user_input)

    # Show assistant message
    with st.chat_message("assistant"):
        st.markdown(f"🧠 **Agent:** {agent}\n\n{response}")

    st.session_state.messages.append({
        "role": "assistant",
        "content": f"🧠 Agent: {agent}\n\n{response}"
    })