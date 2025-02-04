import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

#Define the tickers for Soitec, Nvidia, MSFT, AAPL, BTC, and ATOS
all_tickers = ['SOI.PA', 'NVDA', 'MSFT', 'AAPL', 'ATOS']

#Function to fetch data for the past 20 years from today
def get_data(tickers):
data = yf.download(tickers, start="2022-01-01")
return data['Close']

#Fetch and process the data
close_prices = get_data(all_tickers)

#Main title of the page
st.title('Le Jean Yves Chart: SOI et le reste')

£#Display a dropdown to select companies for comparison
selected_companies = st.multiselect('Select Companies', all_tickers, default=all_tickers[:2])
if not selected_companies:
st.error("Please select at least one company to compare.")
else:
# Filter the close prices based on selected companies
close_prices = get_data(selected_companies)

# Plotting using plotly-express for interactivity
fig = px.line(close_prices, labels={'value': 'Closing Price', 'index': 'Date'})
st.plotly_chart(fig)
