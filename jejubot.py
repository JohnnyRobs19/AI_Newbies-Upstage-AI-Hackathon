import streamlit as st

st.title("AINewbies Tourism GPT")

message = st.chat_message("assistant")
message.write("Hello")


prompt = st.chat_input("Ask something about Jeju Island")