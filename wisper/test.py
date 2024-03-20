import requests
import time

with open("user_message.wav", "rb") as wav_file:
    file_data = wav_file.read()
    file_data = {"file": file_data}

data = {'question': "How motivated do you feel about coming back to our rehabilitation session after today's session?"}

start_time = time.time()
response = requests.post("http://127.0.0.1:8000/chat_with_llm", files=file_data, data=data)
print(time.time()-start_time)

with open("output.wav", "wb") as file:
    file.write(response.content)