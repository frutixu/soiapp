import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Define the tickers for Soitec and Nvidia
tickers = ['SOI.PA', 'NVDA']

# Fetch data for the past 20 years from today
data = yf.download(tickers, start="2003-01-01")

# Extract closing prices
close_prices = data['Close']
close_prices.columns = ['SOITEC', 'NVDA']


# Plotting using plotly-express for interactivity
fig = px.line(close_prices, title='Stock Price Comparison: Soitec SA (SOIT) vs Nvidia (NVDA) aka Jean yves chart', labels={'value':'Closing Price', 'index': 'Date'})
st.plotly_chart(fig)
