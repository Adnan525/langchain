# took 86 seconds on cpu

from langchain_core.prompts import ChatPromptTemplate #initial setup
from langchain_core.output_parsers import StrOutputParser #default output parser
from langchain_community.llms import Ollama

import streamlit as st #web app
import os
from dotenv import load_dotenv

load_dotenv()
# langsmith
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("langchain_api_key") # monitoring

## prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a personal asistant, please response to user queries precisely and accurately."),
    ("user", "Question:{question}")
])

# streamlit
st.title("Langchain OLLAMA Open Source Chat")
input_text = st.text_input("Enter your question here:")

# openai
llm = Ollama(model = "gemma:2b")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))