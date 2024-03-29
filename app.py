from langchain_community.llms import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
import streamlit as st
def get_openai_response(question):
    llm=OpenAI(model_name="text-davinci-003",temperature=0.5)
    response=llm(question)