import dotenv
import os
import requests

dotenv.load_dotenv()
api_key: str = os.getenv("API_KEY")
search_engine_id: str = os.getenv("SEARCH_ENGINE_ID")

def search(query: str, num_results: int=10):
    url: str = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": search_engine_id,
        "q": query,
        "num": num_results,
    }
    response: requests.Response = requests.get(url, params=params)
    response.raise_for_status()

    encoded_response = response.json()
    return encoded_response