import requests
import json

# Base URL for the FastAPI server
BASE_URL = "http://localhost:8000"

def test_root_endpoint():
    """Test the GET / endpoint"""
    print("Testing GET / endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        print("-" * 50)
    except requests.exceptions.RequestException as e:
        print(f"Error testing root endpoint: {e}")
        print("-" * 50)

def test_store_json_endpoint():
    """Test the POST /store-json endpoint"""
    print("Testing POST /store-json endpoint...")
    
    # Sample JSON data to send
    test_data = {
        "name": "Test User",
        "email": "test@example.com",
        "age": 25,
        "hobbies": ["reading", "coding", "music"]
    }
    
    try:
        response = requests.post(f"{BASE_URL}/store-json", json=test_data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        print("-" * 50)
    except requests.exceptions.RequestException as e:
        print(f"Error testing store-json endpoint: {e}")
        print("-" * 50)

def test_get_jsons_endpoint():
    """Test the GET /get-jsons endpoint"""
    print("Testing GET /get-jsons endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/get-jsons")
        print(f"Status Code: {response.status_code}")
        json_files = response.json()
        print(f"Number of JSON files found: {len(json_files)}")
        
        # Print each JSON file content (first 100 chars for readability)
        for i, json_content in enumerate(json_files, 1):
            print(f"JSON File {i} (first 100 chars): {json_content[:100]}...")
        print("-" * 50)
    except requests.exceptions.RequestException as e:
        print(f"Error testing get-jsons endpoint: {e}")
        print("-" * 50)

def main():
    """Run all tests"""
    print("Starting FastAPI Server Tests")
    print("=" * 50)
    
    # Test all endpoints
    test_root_endpoint()
    test_store_json_endpoint()
    test_get_jsons_endpoint()
    
    print("All tests completed!")

if __name__ == "__main__":
    main()
