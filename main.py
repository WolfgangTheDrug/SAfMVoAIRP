import src.api_client.google_search as gs

import json

if __name__ == "__main__":
    result = gs.search('+"Artificial Intelligence" -"Machine Learning"')
    print(json.dumps(result, indent=4))