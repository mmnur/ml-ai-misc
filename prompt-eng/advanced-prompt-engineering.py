# Pre-req: Install required libraries
# pip install langchain-google-genai langchain-core

import os
from getpass import getpass
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ["GOOGLE_API_KEY"] = getpass("Enter your API key: ")

# Use the ChatGoogleGenerativeAI class for the Gemini model integration
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)

# Create a prompt template using LangChain ChatPromptTemplate
template = """
Question: {question}
Answer: Let's think step by step.
"""
prompt = ChatPromptTemplate.from_template(template)

# Create a chain to connect the prompt, the model, and an output parser.
chain = prompt | llm | StrOutputParser()

# Run
question = "Quantum Computing"
print("Running Gemini Model Chain ")
response = chain.invoke({"question": question})
print(f"\nQuestion: {question}")
print(f"Answer: {response.strip()}")

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os
from getpass import getpass

os.environ["GOOGLE_API_KEY"] = getpass("Your API here")

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)

prompt = "Explain quantum computing in simple terms."

# Zero-shot prompt
response = model.invoke([HumanMessage(content=prompt)])
print(response.content)

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)

# Few-Shot Prompting Technique
messages = [
    HumanMessage(content="Classify the sentiment: 'I love this product!'"),
    AIMessage(content="Positive"),
    HumanMessage(content="Classify the sentiment: 'This is terrible.'"),
    AIMessage(content="Negative"),
    HumanMessage(content="Classify the sentiment: 'It's okay, nothing special.'")
]
response = model.invoke(messages)
print(response.content)
