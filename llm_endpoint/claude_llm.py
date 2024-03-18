from llm import LLM
import anthropic

class ClaudeLLM(LLM):
    def __init__(self, api_key: str, model: str = "claude-3-opus-20240229" , context_length: int = 512, temperature: float = 0.0):
        self.client = anthropic.Anthropic(
                        api_key=api_key,
                    )
        self.model = model
        self.context_length = context_length
        self.temperature = temperature

    def llm_response(self, chat_message: str, system_message: str) -> str:
        """
        Does llm chat completion.

        :param chat_message: The message you want to send to gemini.
        :return: LLM's chat completion.
        """
        message = self.client.messages.create(
            model=self.model,
            max_tokens=self.context_length,
            temperature=self.temperature,
            system=system_message,
            messages=[
                {"role": "user", "content": chat_message}
            ]
        )
        
        return message.content[0].text
