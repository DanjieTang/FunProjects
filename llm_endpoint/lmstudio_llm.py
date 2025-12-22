import requests
import json
import base64
from llm import LLM

class LMStudioLLM(LLM):
    def __init__(self, url: str = "http://localhost:1234/v1/chat/completions", stream: bool = False, model: str = "llama2:latest"):
        self.url = url
        self.stream = stream
        self.model = model

    def encode_image(self, image_path: str) -> str:
        """Converts an image file to a base64 string."""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    
    def llm_response(self, user_message: str, image_path: str | None = None, system_message: str = "You are a helpful assistant.") -> str:
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
            "messages": [
                {
                    "role": "system", 
                    "content": system_message
                },
                {
                    "role": "user", 
                    "content": user_message
                }
            ]
        }
        if image_path:
            data["messages"][-1]["content"] = [
                {"type": "text", "text": user_message},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{self.encode_image(image_path)}"
                    }
                }
            ]
        response = requests.post(self.url, headers=header, data=json.dumps(data))
        
        # Check for error
        if response.status_code == 200:
            return json.loads(response.text)["choices"][0]["message"]["content"]
        else:
            raise Exception("Something went wrong")