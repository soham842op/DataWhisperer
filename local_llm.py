from llama_cpp import Llama
from langchain_core.runnables import Runnable
from typing import Dict, Any

class MistralLocalLLM(Runnable):
    def __init__(self, model_path: str):
        self.model = Llama(model_path=model_path, n_gpu_layers=-1, n_ctx=2048)

    def invoke(self, input, config: Any = None, **kwargs: Any) -> str:
        # Accept both plain string and dict input
        if isinstance(input, dict):
            prompt = input.get("query") or input.get("question")
        else:
            # For StringPromptValue or raw str
            prompt = str(input)

        if not prompt:
            raise ValueError("No input prompt provided.")

        output = self.model(prompt, max_tokens=512)
        return output["choices"][0]["text"].strip()
