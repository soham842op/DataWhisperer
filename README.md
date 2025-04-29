# 🧠 DataWhisperer: Local SQL-Powered AI Agent

This project builds an offline, GPU-accelerated AI agent that uses [Mistral 7B](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) to answer natural language questions about structured data using SQL.

## 🚀 Features
- Uses `llama-cpp-python` to run Mistral 7B locally (no OpenAI or cloud needed)
- LangChain `SQLDatabaseChain` to turn natural language → SQL queries
- Fully works offline after model download
- Fast performance using GPU (RTX 4070 or higher recommended)

## 🗂️ Folder Structure

