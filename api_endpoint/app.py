from fastapi import FastAPI
from langserve import add_routes
import uvicorn as uv

import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("openai_api_key")
#langsmith
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("langchain_api_key")

app = FastAPI(
    title="Langchain Chat API",
    version="1.0",
    description="This is a chat API that uses OpenAI and Ollama models" 
)

gpt_llm = ChatOpenAI(model = "gpt-3.5-turbo")
ollama_llm = Ollama(model = "gemma:2b")

# use same prompt for both models
prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a personal asistant, please response to user queries precisely and accurately."),
        ("user", "Question:{question}")
    ])

add_routes(app, prompt|gpt_llm, path = "/gpt")
add_routes(app, prompt|ollama_llm, path = "/ollama")

if __name__ == "__main__":
    uv.run(app, host="localhost", port=8000)