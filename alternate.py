import streamlit as st
import yfinance as finance
import requests

def getTicker(company_name):
    yfinance = "https://query2.finance.yahoo.com/v1/finance/search"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    params = {"q": company_name, "quotes_count": 1, "country": "United States"}

    res = requests.get(url=yfinance, params=params, headers={'User-Agent': user_agent})
    data = res.json()

    company_code = data['quotes'][0]['symbol']
    return company_code

def get_company_ticker(name):
	company = finance.Ticker(name)
	return company

st.markdown("<h1 style='text-align: center; color: white;'>DATATAILR STOCK APP</h1>", unsafe_allow_html=True)


company_full_name  = st.text_input(label = "Company Name")
company_name = getTicker(company_full_name)
start_date = st.text_input(label = "Start Date")
end_date = st.text_input(label="End Date")
company = get_company_ticker(company_name)
data_download = finance.download(company_name, start=start_date, end=end_date)
data = company.history(period = '1mo')
st.write("\n\n\n")
st.write(company_full_name.upper())
st.write(company.info['longBusinessSummary'])
st.write(data_download)
st.line_chart(data.values)