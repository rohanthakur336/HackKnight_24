import pandas as pd
from sklearn.linear_model import LinearRegression

def forecast_revenue(df, years=5):
    X = df['FiscalYearEnd'].values.reshape(-1, 1)
    y = df['TotalRevenue'].values
    model = LinearRegression()
    model.fit(X, y)
    future_years = [[year] for year in range(df['FiscalYearEnd'].max() + 1, df['FiscalYearEnd'].max() + 1 + years)]
    future_revenue = model.predict(future_years)
    return future_years, future_revenue

if __name__ == "__main__":
    df = pd.read_csv('/Users/rohanthakur/Desktop/HackKnight_24/financial-foresight/data/sample_data.csv')
    years, revenue = forecast_revenue(df)
    print(f'Projected Revenue for the next {len(years)} years:', revenue)
