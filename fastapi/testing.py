import requests

response = requests.post("http://127.0.0.1:8000?content=Hello world")
print(response.json())

response = requests.get("http://127.0.0.1:8000/0")
print(response.json())

response = requests.put("http://127.0.0.1:8000/0?content=Ending soon")
print(response.json())

response = requests.delete("http://127.0.0.1:8000/0")
print(response.json())