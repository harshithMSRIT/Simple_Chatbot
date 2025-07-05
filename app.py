from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = ""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "enter the prompt to search"),
        ("user", "Question")
])

st.title("this is a chatbot")
input = st.text_input("enter the prompt here")

llm = ChatOpenAI(model = "gpt-4o")
output = StrOutputParser()
chain = prompt|llm|output

if input :
    st.write(chain.invoke({'Question':input}))