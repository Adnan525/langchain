import streamlit as st
import requests

def call_gpt(input_text):
    url = "http://localhost:8000/gpt/invoke"
    data = {"input":{"question":input_text}}
    response = requests.post(url, json = data)
    return response.json()["output"]["content"] # different for openai

def call_gemma(input_text):
    url = "http://localhost:8000/ollama/invoke"
    data = {"input":{"question":input_text}}
    response = requests.post(url, json = data)
    return response.json()["output"]

st.title("Langchain Chat API")
gpt_text = st.text_input("Ask GPT-3.5 Turbo")
ollama_text = st.text_input("Ask Gemma:2b")

if gpt_text:
    st.write(call_gpt(gpt_text))

if ollama_text:
    st.write(call_gemma(ollama_text))