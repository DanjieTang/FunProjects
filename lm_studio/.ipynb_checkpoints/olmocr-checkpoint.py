from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio", timeout=60)