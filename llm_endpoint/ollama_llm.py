import requests
import json
from llmendpoint.llm import LLM

class OllamaLLM(LLM):
    def __init__(self, url: str = "http://localhost:11434/api/generate", stream: bool = False, model: str = "llama2:latest"):
        self.url = url
        self.stream = stream
        self.model = model
    
    def llm_response(self, user_message: str, system_message: str = "You are a helpful assistant.") -> str:
        """
        Call hosted ollama llm and return the response.
        
        :param user_message: User message.
        :param system_message: System message.
        :return: The model message.
        """
        header = { # Hardcoded. As far as I am concerned, header never changes.
            "Content-Type": "application/json",
        }
        data = {
            "model": self.model,
            "stream": self.stream,
            "system": system_message,
            "prompt": user_message
        }
        response = requests.post(self.url, headers=header, data=json.dumps(data))
        
        # Check for error
        if response.status_code == 200:
            return json.loads(response.text)["response"]
        else:
            raise Exception("Something went wrong")