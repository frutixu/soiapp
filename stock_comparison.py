import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Define the tickers for Soitec and Nvidia
tickers = ['SOI.PA', 'NVDA']

# Fetch data for the past 20 years from today
data = yf.download(tickers, start="2018-01-01")

# Extract closing prices
close_prices = data['Close']
close_prices.columns = ['SOITEC', 'NVDA']


# Plotting using plotly-express for interactivity
fig = px.line(close_prices, title='Jean Yves Chart: Soitec SA (SOI) vs Nvidia (NVDA)', labels={'value':'Closing Price', 'index': 'Date'})
st.plotly_chart(fig)
