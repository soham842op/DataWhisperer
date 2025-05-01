# 🧠 DataWhisperer: Local SQL-Powered AI Agent

This project builds an offline, GPU-accelerated AI agent that uses [CodeLLama](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) to answer natural language questions about structured data using SQL.

## 🚀 Features
- Uses `llama-cpp-python` to run CodeLlama locally (no OpenAI or cloud needed)
- LangChain `SQLDatabaseChain` to turn natural language → SQL queries
- Fully works offline after model download
- Fast performance using GPU (RTX 4070 or higher recommended)

## 🗂️ Folder Structure

📁 DataWhisperer/  ├── sql_agent.py # Main loop: ask questions to CodeLlama  <br>
                    ├── local_llm.py # LangChain-compatible wrapper for Mistral <br>
                    ├── setup_db.py # Creates sample sales.db SQLite database <br>
                    ├── sales.db # SQLite file with sample data <br>
                    ├── .env.example # Example token/env template <br>
                    ├── requirements.txt # Python dependencies <br>
                    ├── .gitignore # Prevents model files & secrets from uploading <br> 
                    └── models/ # Contains GGUF model (NOT included in repo) <br>
                    └── codellama-7b-instruct.Q4_K_M.gguf <br>


---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/datawhisperer.git
cd datawhisperer
```

### 2. Create virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
⚠️ Note: GPU support via llama-cpp-python requires CUDA 12.1+. For prebuilt wheels:
```bash
pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir --prefer-binary --extra-index-url https://jllllll.github.io/llama-cpp-python-cuBLAS-wheels/AVX2/cu121/
```
### 4. Download the CodeLLama model (GGUF format)
Download from: TheBloke/codellama-7b-instruct.Q4_K_M.gguf
Place it here:
```bash
models/codellama-7b-instruct.Q4_K_M.gguf
```
### 5. Create the SQLite database
```bash
python setup_db.py
```

🚀 Launch the App
```bash
streamlit run app.py
```

You’ll be prompted to ask questions:

❓ "How many laptops were sold?"
❓ "Which product had the highest revenue?"
❓ "Total revenue for tablets sold after March?"

Your local agent will:

* 🧠 Use CodeLLama to generate SQL
* 🔍 Query the SQLite database
* 💬 Return the result

🔐 Environment File
Create a .env file (or rename .env.example) if you want to test with Hugging Face or OpenAI models later.
```bash
HUGGINGFACEHUB_API_TOKEN=your_token_here
```
🚫 .gitignore
```bash
.env
models/
*.gguf
__pycache__/
```
📦 Dependencies
```bash 
streamlit
langchain
langchain-community
langchain-experimental
llama-cpp-python
python-dotenv
sqlite3
pandas
```
