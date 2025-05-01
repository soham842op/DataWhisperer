from llama_cpp import Llama
from langchain_core.runnables import Runnable
from typing import Dict, Any
import re


class MistralLocalLLM(Runnable):
    def __init__(self, model_path: str):
        self.model = Llama(
            model_path=model_path,
            n_gpu_layers=-1,
            n_ctx=2048,
            f16_kv=True,
            use_mlock=True,
            n_threads=8
        )

    def invoke(self, input: Dict[str, Any], config=None, **kwargs) -> str:
        if isinstance(input, dict):
            prompt = input.get("query") or input.get("question")
        else:
            prompt = str(input)

        if not prompt:
            raise ValueError("No input prompt provided.")

        # ✅ Apply CodeLlama instruction-style format
        prompt = f"<s>[INST] You are an AI that writes SQLite-compatible SQL queries.\n{prompt.strip()} [/INST]"

        # 🔮 Run model inference
        output = self.model(prompt, max_tokens=512, temperature=0.2)
        raw = output["choices"][0]["text"]

        # 🧹 Strip LangChain wrappers like [SQL: ...]
        raw = re.sub(r"^\[SQL:\s*", "", raw, flags=re.IGNORECASE)
        raw = raw.strip().rstrip("]").strip()

        # 🧽 Clean and normalize the SQL string
        cleaned = raw.replace("\n", " ").replace('"', "'").replace("`", "'").strip()
        if not cleaned.endswith(";"):
            cleaned += ";"

        return cleaned
