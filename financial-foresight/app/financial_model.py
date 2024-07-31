# import pandas as pd
# from sklearn.linear_model import LinearRegression

# def forecast_revenue(df, years=5):
#     future_years_list = []
#     future_revenue_list = []

#     for index, row in df.iterrows():
#         X = df.loc[:index, 'FiscalYearEnd'].values.reshape(-1, 1)
#         y = df.loc[:index, 'TotalRevenue'].values
#         model = LinearRegression()
#         model.fit(X, y)
#         future_years = [[year] for year in range(df['FiscalYearEnd'].max() + 1, df['FiscalYearEnd'].max() + 1 + years)]
#         future_revenue = model.predict(future_years)
#         future_years_list.append(future_years)
#         future_revenue_list.append(future_revenue)

#     return future_years_list, future_revenue_list

# if __name__ == "__main__":
#     df = pd.read_csv('/Users/rohanthakur/Desktop/HackKnight_24/financial-foresight/data/sample_data.csv')
#     years_list, revenue_list = forecast_revenue(df)
#     for index, (years, revenue) in enumerate(zip(years_list, revenue_list)):
#         print(f'Projected Revenue for row {index + 1} for the next {len(years)} years:', revenue)

# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error, mean_squared_error
# import numpy as np

# def forecast_revenue(df, years=5):
#     future_years_list = []
#     future_revenue_list = []
#     mae_list = []
#     rmse_list = []
    
#     for i in range(len(df)):
#         # Use data up to the current row for training
#         train_df = df.iloc[:i+1]
#         if len(train_df) < 2:  # Need at least two points to fit a model
#             continue
        
#         X_train = train_df['FiscalYearEnd'].values.reshape(-1, 1)
#         y_train = train_df['TotalRevenue'].values
        
#         # Prepare test data
#         test_df = df.iloc[i+1:i+1+years]
#         if test_df.empty:
#             continue
        
#         X_test = test_df['FiscalYearEnd'].values.reshape(-1, 1)
#         y_test = test_df['TotalRevenue'].values
        
#         model = LinearRegression()
#         model.fit(X_train, y_train)
        
#         # Predict future revenue
#         future_years = [[year] for year in range(train_df['FiscalYearEnd'].max() + 1, train_df['FiscalYearEnd'].max() + 1 + years)]
#         future_revenue = model.predict(future_years)
        
#         # Predict on test data
#         if len(y_test) > 0:
#             y_pred = model.predict(X_test)
#             mae = mean_absolute_error(y_test, y_pred)
#             rmse = np.sqrt(mean_squared_error(y_test, y_pred))
#         else:
#             mae = rmse = np.nan  # Not enough data to calculate metrics
        
#         future_years_list.append(future_years)
#         future_revenue_list.append(future_revenue)
#         mae_list.append(mae)
#         rmse_list.append(rmse)
    
#     return future_years_list, future_revenue_list, mae_list, rmse_list

# if __name__ == "__main__":
#     df = pd.read_csv('/Users/rohanthakur/Desktop/HackKnight_24/financial-foresight/data/sample_data.csv')
#     future_years_list, future_revenue_list, mae_list, rmse_list = forecast_revenue(df)
    
#     for index, (years, revenue, mae, rmse) in enumerate(zip(future_years_list, future_revenue_list, mae_list, rmse_list)):
#         print(f'\nRow {index + 1}:')
#         print(f'Projected Revenue for the next {len(years)} years:', revenue)
#         print(f'Mean Absolute Error (MAE): {mae}')
#         print(f'Root Mean Squared Error (RMSE): {rmse}')

# import pandas as pd
# from sklearn.linear_model import LinearRegression, Ridge, Lasso
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.svm import SVR
# from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error
# from sklearn.model_selection import cross_val_score, KFold, GridSearchCV
# from sklearn.preprocessing import StandardScaler, PolynomialFeatures
# import numpy as np

# def get_best_model(X, y):
#     models = {
#         'LinearRegression': LinearRegression(),
#         'Ridge': Ridge(),
#         'Lasso': Lasso(),
#         'RandomForest': RandomForestRegressor(),
#         'SVR': SVR()
#     }
    
#     best_model = None
#     best_score = float('inf')
#     best_model_name = ""
    
#     # Use at most min(len(X), 5) folds for cross-validation
#     num_folds = min(len(X), 5)
#     if num_folds < 2:
#         return LinearRegression().fit(X, y)  # Return a simple model if not enough data for CV
    
#     kf = KFold(n_splits=num_folds)
    
#     for name, model in models.items():
#         scores = cross_val_score(model, X, y, scoring='neg_mean_squared_error', cv=kf)
#         mean_score = -np.mean(scores)
#         if mean_score < best_score:
#             best_score = mean_score
#             best_model = model
#             best_model_name = name
    
#     best_model.fit(X, y)
#     print(f"Best model selected: {best_model_name} with MSE: {best_score}")
#     return best_model

# def forecast_revenue(df, years=5):
#     future_years_list = []
#     future_revenue_list = []
#     mae_list = []
#     rmse_list = []
#     mape_list = []
    
#     scaler = StandardScaler()
#     poly = PolynomialFeatures(degree=2)  # Try polynomial features for non-linear relationships
    
#     for i in range(len(df)):
#         # Use data up to the current row for training
#         train_df = df.iloc[:i+1]
#         if len(train_df) < 2:  # Need at least two points to fit a model
#             continue
        
#         X_train = train_df['FiscalYearEnd'].values.reshape(-1, 1)
#         X_train_poly = poly.fit_transform(X_train)
#         X_train_scaled = scaler.fit_transform(X_train_poly)
#         y_train = train_df['TotalRevenue'].values
        
#         # Prepare test data
#         test_df = df.iloc[i+1:i+1+years]
#         if test_df.empty:
#             continue
        
#         X_test = test_df['FiscalYearEnd'].values.reshape(-1, 1)
#         X_test_poly = poly.transform(X_test)
#         X_test_scaled = scaler.transform(X_test_poly)
#         y_test = test_df['TotalRevenue'].values
        
#         model = get_best_model(X_train_scaled, y_train)
        
#         # Predict future revenue
#         future_years = np.array(range(train_df['FiscalYearEnd'].max() + 1, train_df['FiscalYearEnd'].max() + 1 + years)).reshape(-1, 1)
#         future_years_poly = poly.transform(future_years)
#         future_years_scaled = scaler.transform(future_years_poly)
#         future_revenue = model.predict(future_years_scaled)
        
#         # Predict on test data
#         if len(y_test) > 0:
#             y_pred = model.predict(X_test_scaled)
#             mae = mean_absolute_error(y_test, y_pred)
#             rmse = np.sqrt(mean_squared_error(y_test, y_pred))
#             mape = mean_absolute_percentage_error(y_test, y_pred)
#         else:
#             mae = rmse = mape = np.nan  # Not enough data to calculate metrics
        
#         future_years_list.append(future_years)
#         future_revenue_list.append(future_revenue)
#         mae_list.append(mae)
#         rmse_list.append(rmse)
#         mape_list.append(mape)
    
#     return future_years_list, future_revenue_list, mae_list, rmse_list, mape_list

# if __name__ == "__main__":
#     df = pd.read_csv('/Users/rohanthakur/Desktop/HackKnight_24/financial-foresight/data/sample_data.csv')
#     future_years_list, future_revenue_list, mae_list, rmse_list, mape_list = forecast_revenue(df)
    
#     for index, (years, revenue, mae, rmse, mape) in enumerate(zip(future_years_list, future_revenue_list, mae_list, rmse_list, mape_list)):
#         print(f'\nRow {index + 1}:')
#         print(f'Projected Revenue for the next {len(years)} years:', revenue)
#         print(f'Mean Absolute Error (MAE): {mae}')
#         print(f'Root Mean Squared Error (RMSE): {rmse}')
#         print(f'Mean Absolute Percentage Error (MAPE): {mape}')

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
