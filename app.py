import streamlit as st
from openai import OpenAI

import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


st.title("Survey AI Assistant 🤖")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Ask your question:")

if st.button("Send"):
    if user_input:
        st.session_state.chat.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert in Forsta (Decipher) surveys. Give clear and helpful answers."
                }
            ] + st.session_state.chat
        )

        reply = response.choices[0].message.content
        st.session_state.chat.append({"role": "assistant", "content": reply})

# Display chat
for msg in st.session_state.chat:
    if msg["role"] == "user":
        st.write(f"👤 You: {msg['content']}")
    else:
        st.write(f"🤖 AI: {msg['content']}")