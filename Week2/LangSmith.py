from dotenv import load_dotenv
import os

# Load all environment variables from .env
load_dotenv()

# ----------------------------------------
# LangChain Imports
# ----------------------------------------
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ----------------------------------------
# Create Prompt, Model, Parser
# ----------------------------------------
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in one simple sentence."
)

model = ChatOpenAI(
    model="gpt-4o-mini"
)

output_parser = StrOutputParser()

# ----------------------------------------
# Create Chain
# ----------------------------------------
chain = prompt | model | output_parser

print("========== LangChain ==========")

response = chain.invoke({"topic": "LangSmith"})

print(response)

# ----------------------------------------
# LangSmith Traceable Function
# ----------------------------------------
from langsmith import traceable

@traceable
def make_greeting(name):
    return f"Hello {name}, welcome to GenAI!"

print("\n========== Traceable Function ==========")
print(make_greeting("Priya Senthil"))

# ----------------------------------------
# OpenAI SDK + LangSmith Tracking
# ----------------------------------------
from openai import OpenAI
from langsmith.wrappers import wrap_openai

client = wrap_openai(OpenAI())

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Say hello in one word."
        }
    ]
)

print("\n========== OpenAI SDK ==========")
print(response.choices[0].message.content)