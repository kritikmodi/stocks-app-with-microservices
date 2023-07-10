from flask import Flask, request
import yfinance as finance
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/1', methods=['POST'])
def index1():
    company_code = request.form['text']
    company_ticker = finance.Ticker(company_code)
    return company_ticker.info['longBusinessSummary']

@app.route('/2', methods=['POST'])
def index2():
    company_code = request.form['text']
    company_ticker = finance.Ticker(company_code)
    company_finance_details = finance.download(company_code, start="2022-04-01", end="2022-09-01")
    return company_finance_details.to_string(index=True)

@app.route('/3', methods=['POST'])
def index3():
    company_code = request.form['text']
    company_ticker = finance.Ticker(company_code)
    company_data = company_ticker.history(period="1mo")
    df = pd.DataFrame(company_data.values)
    return df.to_string(index=False)
    
if __name__ == '__main__':
    app.run()