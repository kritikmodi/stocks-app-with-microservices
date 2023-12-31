import streamlit as st
import requests
import pandas as pd
from io import StringIO
import numpy as np

def send_request(company_code,x):
    try:
        url = 'http://127.0.0.1:5000/'+x
        payload = {'text': company_code}
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(e)
        return None

def display_results(company_info,company_finance,company_data):
    st.write("\n\n\n")
    st.write("""### {company_ticker}""")
    st.write(company_info)
    st.write(pd.read_csv(StringIO(company_finance), sep='\s+'))
    st.line_chart(pd.read_csv(StringIO(company_data), sep='\s+'))

def main():
    st.markdown("<h1 style='text-align: center; color: white;'>DATATAILR STOCK APP</h1>", unsafe_allow_html=True)
    st.title('Enter company code')
    company_code = st.text_input('Enter some text')
    if st.button('Submit'):
        company_info = send_request(company_code,"1")
        company_finance = send_request(company_code,"2")
        company_data = send_request(company_code,"3")
        if company_info is not None:
            display_results(company_info,company_finance,company_data)
        else:
            st.write('Error: Failed to connect to Flask service.')
    
if __name__ == '__main__':
    main()