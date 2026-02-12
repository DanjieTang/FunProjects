import requests

url = "https://divertingly-unmaterialised-zandra.ngrok-free.dev"

# Ngrok free accounts require this header to bypass the 
# "You are about to visit..." warning page.
headers = {
    "ngrok-skip-browser-warning": "69420"
}

try:
    # Send the GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    response.raise_for_status()

    # Print the output
    print("Status Code:", response.status_code)
    
    # Use .json() if the endpoint returns JSON, otherwise use .text
    try:
        print("Response Body (JSON):", response.json())
    except ValueError:
        print("Response Body (Text):", response.text)

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"An error occurred: {err}")