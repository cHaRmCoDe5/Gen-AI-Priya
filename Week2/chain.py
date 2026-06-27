from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ---------------------------------------
# Load API Key from .env
# ---------------------------------------
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# ---------------------------------------
# Create Chat Model
# ---------------------------------------
model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=api_key
)

# ---------------------------------------
# Create Output Parser
# ---------------------------------------
output_parser = StrOutputParser()

# ---------------------------------------
# Chain 1 - Explain a Topic
# ---------------------------------------
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in one simple sentence."
)

chain = prompt | model | output_parser

print("✅ Chain 1 is ready!")

answer = chain.invoke({"topic": "Python"})

print("\nExplanation:")
print(answer)

# ---------------------------------------
# Chain 2 - Give a Learning Tip
# ---------------------------------------
tip_prompt = ChatPromptTemplate.from_template(
    "Give one short, friendly tip for a beginner learning {skill}."
)

tip_chain = tip_prompt | model | output_parser

print("\n✅ Chain 2 is ready!")

tip = tip_chain.invoke({"skill": "Python"})

print("\nTip:")
print(tip)