import pandas as pd

def process_data(filename='data/sample_data.csv'):
    df = pd.read_csv(filename)
    df['P/E Ratio'] = df['MarketCapitalization'] / df['NetIncome']
    df['Debt/Equity Ratio'] = df['TotalDebt'] / df['ShareholdersEquity']
    return df

if __name__ == "__main__":
    df = process_data()
    print(df.head())
