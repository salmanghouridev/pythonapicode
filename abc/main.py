from flask import Flask, request, render_template, send_from_directory
import numpy as np
from py_vollib.black.implied_volatility import implied_volatility as iv
from py_vollib.black.greeks.numerical import delta, theta, gamma, vega
import requests
import pandas as pd
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_DIR = os.path.join(BASE_DIR, 'temp_excel_files')

if not os.path.exists(EXCEL_DIR):
    os.mkdir(EXCEL_DIR)

computed_data = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', data=[])

@app.route('/read', methods=['POST'])
def read_api():
    api_url = request.form['api_url']
    # Fetch the data from the provided API
    response = requests.get(api_url)
    data = response.json()
    # For now, save this data in a global variable (not recommended for production)
    global api_data
    api_data = data[:1000000]  # Fetching first 10 data points
    return render_template('index.html', data=[])

@app.route('/generate', methods=['GET'])
def generate_data():
    global api_data, computed_data
    results = []

    # Compute metrics for each data point
    for item in api_data:
        d = item['days_to_expiry'] / 365
        e = iv(item['strike_price'], item['underlying_price'], item['strike'], 0.01, d, item['type'])
        a = delta(item['type'], item['underlying_price'], item['strike'], d, 0.1, e)
        b = theta(item['type'], item['underlying_price'], item['strike'], d, 0.1, e)
        c = gamma(item['type'], item['underlying_price'], item['strike'], d, 0.1, e)
        d = vega(item['type'], item['underlying_price'], item['strike'], d, 0.1, e)

        results.append({
            'timestamp': item['timestamp'],
            'token': item['token'],
            'symbol': 'XYZ',
            'IV': round(e*100,2),
            'delta': round(a,2),
            'theta': round(b,0),
            'vega': round(c,4),
            'gamma': round(d,0)
        })

    # Save the computed data for downloading
    computed_data = results
    
    return render_template('index.html', data=results)

@app.route('/download', methods=['GET'])
def download_excel():
    global computed_data

    # Debug print to verify computed_data
    print("Computed Data:", computed_data)

    df = pd.DataFrame(computed_data)

    # Debug print to verify the DataFrame creation
    print("DataFrame:\n", df)

    filename = "generated_data.xlsx"
    filepath = os.path.join(EXCEL_DIR, filename)
    df.to_excel(filepath, index=False, engine='openpyxl')

    return send_from_directory(directory=EXCEL_DIR, path=filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)