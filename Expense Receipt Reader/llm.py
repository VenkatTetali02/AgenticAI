from langchain_openai import OpenAI,ChatOpenAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

llm=ChatGroq(temperature=0.0,model="llama-3.3-70b-versatile")
llm = LLM(
    # model="groq/llama-3.3-70b-versatile",
    model="openai/gpt-4",
    temperature=0.2
)