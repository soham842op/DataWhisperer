from dotenv import load_dotenv
import os

# LangChain & SQL
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

# Local Mistral wrapper (you must have local_llm.py in the same folder)
from local_llm import MistralLocalLLM

# Load environment variables (not required for local models, but kept for flexibility)
load_dotenv()

# Path to your local SQLite database
db = SQLDatabase.from_uri("sqlite:///sales.db")

# Load local Mistral model from GGUF file
llm = MistralLocalLLM(model_path="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf")

# Create LangChain SQL Agent
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

# REPL loop to ask questions
print("✅ Mistral SQL Agent is ready! Ask questions or type 'exit'.\n")

while True:
    question = input("\nAsk your question (or type 'exit'): ")
    if question.lower() in ["exit", "quit"]:
        print("👋 Exiting. Bye!")
        break
    try:
        response = db_chain.invoke({"query": question})
        print("🤖 Agent:", response)
    except Exception as e:
        print("⚠️ Error:", str(e))
