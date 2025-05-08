import os
import dotenv
import src.api_client.google_search as gs
import json

if __name__ == "__main__":
    dotenv.load_dotenv()
    api_key: str = os.getenv("API_KEY")
    search_engine_id: str = os.getenv("SEARCH_ENGINE_ID")

    client: gs.GoogleSearchClient = gs.GoogleSearchClient(api_key, search_engine_id)

    result = client.search(query='+"Artificial Intelligence" -"Machine Learning"', start_date="2020_01")
    print(json.dumps(result, indent=4))