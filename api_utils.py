import requests

BASE_BLOCK_URL = "https://community-api.coinmetrics.io/v4/blockchain-v2/eth/blocks"

response_file_path = "data/response.json"

params = {
    "pretty": "true",  
}

# Fetch block data from the API
def fetch_block_data():
    response = requests.get(BASE_BLOCK_URL, params=params)
    
    if response.status_code == 200:
        with open(response_file_path, "w") as f:
            f.write(response.text)
        print("API data fetched and saved to data/response.json")
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None
