import streamlit as st
from local_llm import MistralLocalLLM
from langchain_community.utilities import SQLDatabase
from patched_chain import PatchedSQLDatabaseChain as SQLDatabaseChain

# Set Streamlit page configuration
st.set_page_config(page_title="DataWhisperer", layout="centered")
st.title("🧠 DataWhisperer - Ask Your Data")

# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.chat_history = []

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User query input
user_query = st.text_input("Ask a question about your data:", placeholder="e.g. How many laptops were sold?")

# Display chat history
for q, a in st.session_state.chat_history:
    st.markdown(f"**You:** {q}")
    st.markdown(f"**Agent:** {a}")

# Load database and LLM
db = SQLDatabase.from_uri("sqlite:///sales.db")
llm = MistralLocalLLM(model_path="models/codellama-7b-instruct.Q4_K_M.gguf")
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

# Run the query and extract clean answer
if user_query:
    try:
        response = db_chain.invoke({"query": user_query})
        if isinstance(response, dict) and "result" in response:
            raw = response["result"]
            for line in raw.splitlines():
                if "Answer:" in line:
                    final_answer = line.strip().split("Answer:")[-1].strip()
                    break
            else:
                final_answer = raw
        else:
            final_answer = str(response)

        st.session_state.chat_history.append((user_query, final_answer))
        st.experimental_set_query_params(clear="true")  # triggers rerun without modifying widget key
        st.rerun()

    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")
