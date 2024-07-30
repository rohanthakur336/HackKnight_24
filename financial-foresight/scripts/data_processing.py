import pandas as pd

def process_data(filename='/Users/rohanthakur/Desktop/HackKnight_24/financial-foresight/data/sample_data.csv'):
    # Read the CSV file
    df = pd.read_csv(filename)
    
    # Calculate the P/E Ratio and Debt/Equity Ratio
    df['P/E Ratio'] = df['MarketCapitalization'] / df['NetIncome']
    df['Debt/Equity Ratio'] = df['TotalDebt'] / df['ShareholdersEquity']
    
    # Save the updated DataFrame back to the CSV file
    df.to_csv(filename, index=False)
    
    return df

if __name__ == "__main__":
    df = process_data()
    print(df.head())
