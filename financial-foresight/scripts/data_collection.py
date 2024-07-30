# import requests
# import pandas as pd

# API_KEY = 'vtz9E5tWs4AV4VzV3HZD'

# def get_financial_data(symbol):
#     url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={API_KEY}'
#     response = requests.get(url)
#     data = response.json()
#     return data

# def save_data_to_csv(data, filename='data/sample_data.csv'):
#     df = pd.DataFrame([data])
#     df.to_csv(filename, index=False)

# if __name__ == "__main__":
#     symbol = 'AAPL'
#     data = get_financial_data(symbol)
#     save_data_to_csv(data,"/Users/rohanthakur/Desktop/HackKnight_24/financial-foresight/data/sample_data.csv")

import quandl
import pandas as pd

# API key for Quandl
API_KEY = 'vtz9E5tWs4AV4VzV3HZD'

def get_financial_data(symbol):
    """
    Fetch financial data for a given symbol from Quandl.

    Args:
    symbol (str): The stock symbol to fetch data for.

    Returns:
    pd.DataFrame: The financial data for the given symbol.
    """
    try:
        quandl.ApiConfig.api_key = API_KEY
        data = quandl.get_table('SHARADAR/SF1', ticker=symbol)
        return data
    except Exception as e:
        print(f"Error: {e}")
        return None

def save_data_to_csv(data, filename):
    """
    Save financial data to a CSV file.

    Args:
    data (pd.DataFrame): The financial data to save.
    filename (str): The path to the CSV file.
    """
    if data is not None and not data.empty:
        data.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    else:
        print("Error: No data to save.")

if __name__ == "__main__":
    symbol = 'AAPL'
    filename = "/Users/rohanthakur/Desktop/HackKnight_24/financial-foresight/data/sample_data.csv"
    
    # Fetch financial data
    data = get_financial_data(symbol)
    
    # Save data to CSV
    save_data_to_csv(data, filename)

