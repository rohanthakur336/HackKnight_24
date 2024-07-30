import requests
import pandas as pd

API_KEY = 'your_alpha_vantage_api_key'

def get_financial_data(symbol):
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data

def save_data_to_csv(data, filename='data/sample_data.csv'):
    df = pd.DataFrame([data])
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    symbol = 'AAPL'
    data = get_financial_data(symbol)
    save_data_to_csv(data)
