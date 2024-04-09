from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

#Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are the most intelligent assistant who helps with whatever questions i ask"),
        ("user","Question:{question}")
    ]
)

#streamlit framework
st.title("Simple LLAMA2 Chatbot")
input_text = st.text_input('Ask me anything!')

#ollama llm
llm = Ollama(model='llama2')
output_parser = StrOutputParser()

chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))

