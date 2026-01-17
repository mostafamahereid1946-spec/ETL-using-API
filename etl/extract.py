import requests
import pandas as pd


def extract_data():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("API request failed")

    data = response.json()
    df = pd.DataFrame(data)

    return df
