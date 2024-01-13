from llm import LLM
import google.generativeai as genai
from PIL import Image

class GeminiLLM(LLM):
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)

    def llm_response(self, chat_message: str, image: Image = None) -> str:
        """
        Does llm chat completion.

        :param chat_message: The message you want to send to gemini.
        :param image: The image you want your llm to see.
        :return: LLM's chat completion.
        """
        if image is not None:
            model = genai.GenerativeModel("gemini-pro-vision")
            chat_message = [chat_message, image]
        else:
            model = genai.GenerativeModel("gemini-pro")

        response = model.generate_content(chat_message)
        return response.text

    def embed(self, sentences: str | list[str]) -> list[float] | list[list[float]]:
        """
        Embed a sentence or multiple sentences.

        :param sentences: Sentence or sentences to be embeded.
        :return: Embedding of sentence or sentences respectively.
        """
        result = genai.embed_content(
            model="models/embedding-001",
            content=sentences,
            task_type="CLASSIFICATION"
        )

        return result["embedding"]