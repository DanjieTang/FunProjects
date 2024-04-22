import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = "https://help.acorn.utoronto.ca/#:~:text=ACORN%20is%20U%20of%20T's,contact%20information%20and%20much%20more."

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the request with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all text within the webpage
    # The 'get_text()' function consolidates all text in the document
    text = soup.get_text(separator=" ", strip=True)
    print(text)
else:
    print("Failed to retrieve the webpage")
