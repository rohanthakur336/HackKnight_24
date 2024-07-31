# # from flask import render_template, request
# # from app import app
# # from scripts.data_collection import load_data_from_csv, save_data_to_csv
# # from scripts.data_processing import process_data
# # from scripts.narrative_generation import generate_narratives
# # from models.financial_model import forecast_revenue

# # @app.route('/')
# # @app.route('/index')
# # def index():
# #     return render_template('index.html')

# # @app.route('/analyze', methods=['POST'])
# # def analyze():
# #     symbol = request.form.get('symbol')
# #     if not symbol:
# #         return render_template('index.html', error="Symbol is required")

# #     # Load data from the CSV file
# #     filename = 'data/sample_data.csv'
# #     df = load_data_from_csv(filename)
# #     if df.empty:
# #         return render_template('index.html', error="No data available")

# #     # Filter the data based on the symbol
# #     df_symbol = df[df['symbol'] == symbol]
# #     if df_symbol.empty:
# #         return render_template('index.html', error=f"No data found for symbol: {symbol}")

# #     # Process the data
# #     df_processed = process_data(df_symbol)
# #     if df_processed.empty:
# #         return render_template('index.html', error="Failed to process data")

# #     # Generate narratives for all rows
# #     narratives = generate_narratives(df_processed)

# #     # Forecast revenue (example implementation for simplicity)
# #     years, revenue = forecast_revenue(df_processed)
# #     forecast_data = dict(zip(years, revenue))
# #     context ={'narratives': narratives, 
# #               'forecast_data': forecast_data,}
# #     return render_template('index.html', context)
# from flask import render_template, request
# from app import app
# from scripts.data_collection import get_financial_data, save_data_to_csv
# from scripts.data_processing import process_data
# from scripts.narrative_generation import generate_narrative
# from models.financial_model import forecast_revenue

# @app.route('/')
# @app.route('/index')
# def index():
#     return render_template('index.html')

# @app.route('/analyze', methods=['POST'])
# def analyze():
#     symbol = request.form['symbol']
#     data = get_financial_data(symbol)
#     save_data_to_csv(data)
#     df_processed = process_data()
#     narrative = generate_narrative(df_processed)
#     years, revenue = forecast_revenue(df_processed)
#     return render_template('index.html', narrative=narrative, years=years, revenue=revenue)

from flask import Blueprint, render_template, request
import pandas as pd
from .financial_model import forecast_revenue
from .data_collection import get_financial_data
from .data_processing import process_data
from .narrative_generation import generate_narrative

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    narrative = None
    years = None
    revenue = None

    if request.method == 'POST':
        symbol = request.form['symbol']
        df = get_financial_data(symbol)
        df = process_data(df)
        narrative = generate_narrative(df)
        years, revenue = forecast_revenue(df)

    return render_template('index.html', narrative=narrative, years=years, revenue=revenue)

@bp.route('/analyze', methods=['POST'])
def analyze():
    symbol = request.form['symbol']
    df = get_financial_data(symbol)
    df = process_data(df)
    narrative = generate_narrative(df)
    years, revenue = forecast_revenue(df)
    return render_template('index.html', narrative=narrative, years=years, revenue=revenue)
