# Pre-req: Install required libraries
# pip install langchain-google-genai langchain-core

import langchain_google_genai
import langchain_core

print(langchain_core.__version__)

import os
from getpass import getpass
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ["GOOGLE_API_KEY"] = getpass("Enter your API key: ")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)

template = """
Question: {question}
Answer: Let's think step by step.
"""
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | llm | StrOutputParser()

question = "Quantum Computing"
print("Running Gemini Model Chain ")
response = chain.invoke({"question": question})
print(f"\nQuestion: {question}")
print(f"Answer: {response.strip()}")
