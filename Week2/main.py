from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# -----------------------------------
# Load API Keys from .env
# -----------------------------------
load_dotenv()

# -----------------------------------
# Create Prompt
# -----------------------------------
prompt = ChatPromptTemplate.from_template("""
You are a helpful Netflix movie recommendation assistant.

Recommend 5 popular Netflix movies that are likely to be trending.

For each movie provide:

Movie Name
Genre
Short Description
Reason to Watch

If you are unsure of the exact current trending list, make your best recommendations based on recent popularity.

Keep the answer neat and easy to read.
""")

# -----------------------------------
# OpenAI Model
# -----------------------------------
model = ChatOpenAI(
    model="gpt-4o-mini"
)

# -----------------------------------
# Output Parser
# -----------------------------------
output_parser = StrOutputParser()

# -----------------------------------
# Create Chain
# -----------------------------------
chain = prompt | model | output_parser

print("=" * 60)
print("🎬 Netflix Trending Movie Recommendation App")
print("=" * 60)

# -----------------------------------
# Run the Chain
# -----------------------------------
response = chain.invoke({})

print("\nTop 5 Recommended Movies\n")
print(response)