from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate #initial setup
from langchain_core.output_parsers import StrOutputParser #default output parser

import streamlit as st #web app
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("openai_api_key")
# langsmith
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("langchain_api_key") # monitoring

## prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a personal asistant, please response to user queries precisely and accurately."),
    ("user", "Question:{question}")
])

# streamlit
st.title("Langchain OpenAI Chat")
input_text = st.text_input("Enter your question here:")

# openai
llm = ChatOpenAI(model = "gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))