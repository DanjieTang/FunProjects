import requests
from dataclass import *

# Prepare the payload. This might change depending on the API's expected format.
payload_create_account = {
    "username": "danjie",
    "password": "your_password",
    "age": 20,
    "real_name": "Danjie"
}

# response = requests.post("http://127.0.0.1:8000/create_account", data=payload_create_account)
# print(response)

# Login
payload_login = {
    "username": "danjie",
    "password": "your_password",
}
# response = requests.post("http://127.0.0.1:8000/login", data=payload_login)
# with open("token.txt", "w") as file:
#     file.write(response.text[1:-1])

# Read authentication token
with open("token.txt", "r") as file:
    token = file.read()

headers = {
    "Authorization": f"Bearer {token}"
}

# Open new store
store_info = {
    "store_name": "Danjie superstore",
    "store_location": "St. Catherine"
}
response = requests.post("http://127.0.0.1:8000/open_store", headers=headers, json=store_info)
print(response.status_code)

# Add item
# item_info = {
#     "item_name": "Bird",
#     "num": 2,
#     "storage_id": 1
# }
# response = requests.post("http://127.0.0.1:8000/add_item", headers=headers, json=item_info)

response = requests.get("http://127.0.0.1:8000/view_all", headers=headers)
print(response)