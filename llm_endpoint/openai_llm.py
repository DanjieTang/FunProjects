from llm_endpoint.llm import LLM
from dotenv import load_dotenv
from os import environ
import openai

class OpenAILLM(LLM):
    def __init__(self, model: str = "gpt-4-1106-preview"):
        load_dotenv()
        openai.api_key = environ["OPENAI_API_KEY"]
        self.model = model
    def llm_response(self, user_message: str, system_message: str = "You are a helpful assistant.") -> str:
        """
        Wrapper for OpenAI chat completion API.
        
        :param user_message: User message.
        :param system_message: System message.
        :return: The model message.
        """
        response = openai.ChatCompletion.create(
            model=self.model,  # or another model like "text-davinci-003"
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ]
        )

        return response['choices'][0]['message']['content']