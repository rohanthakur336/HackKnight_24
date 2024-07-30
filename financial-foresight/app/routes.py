from flask import render_template, request
from app import app
from scripts.data_collection import get_financial_data, save_data_to_csv
from scripts.data_processing import process_data
from scripts.narrative_generation import generate_narrative
from models.financial_model import forecast_revenue

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    symbol = request.form['symbol']
    data = get_financial_data(symbol)
    save_data_to_csv(data)
    df = process_data()
    narrative = generate_narrative(df)
    years, revenue = forecast_revenue(df)
    return render_template('index.html', narrative=narrative, years=years, revenue=revenue)
