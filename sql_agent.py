from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from local_llm import MistralLocalLLM

# Load SQLite database
db = SQLDatabase.from_uri("sqlite:///sales.db")

# Load local CodeLlama model
llm = MistralLocalLLM(model_path="models/codellama-7b-instruct.Q4_K_M.gguf")

# Create LangChain SQL Agent
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

agent_executor = db_chain
