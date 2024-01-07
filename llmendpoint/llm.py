from abc import ABC, abstractclassmethod

class LLM(ABC):
    @abstractclassmethod
    def llm_response(self, user_message: str, system_message: str = "You are a helpful assistant.") -> str:
        pass