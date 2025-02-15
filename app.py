import yfinance as yf
import numpy as np
import pandas as pd
import pandas_ta as ta
import plotly.graph_objects as go
import streamlit as st

# Load Data (Gantilah dengan sumber data yang sesuai)
def collect_data(ticker_name, start_date, end_date):
    data = yf.download(ticker_name, start_date, end_date, multi_level_index = False)
    data['Ticker'] = ticker_name
    return data

date_started = '2009-01-01'
date_ended = '2024-12-30'

btc = collect_data('BTC-USD', date_started, date_ended)
eth = collect_data('ETH-USD', date_started, date_ended)
usdt = collect_data('USDT-USD', date_started, date_ended)
xrp = collect_data('XRP-USD', date_started, date_ended)
sol = collect_data('SOL-USD', date_started, date_ended)
bnb = collect_data('BNB-USD', date_started, date_ended)
usdc = collect_data('USDC-USD', date_started, date_ended)
doge = collect_data('DOGE-USD', date_started, date_ended)
ada = collect_data('ADA-USD', date_started, date_ended)
trx = collect_data('TRX-USD', date_started, date_ended)
df = pd.concat([btc, eth, usdt, xrp, sol, bnb, usdc, doge, ada, trx], axis = 0).reset_index()

def macd(data, fast=12, slow=26, signal=9):
    return ta.macd(data['Close'], fast, slow, signal)

def rsi(data, period=14):
    return ta.rsi(data['Close'], period)

def bbands(data, period=5, std=2):
    return ta.bbands(data['Close'], period, std)

def obv(data):
    return ta.obv(data['Close'], data['Volume'])

macd_vals = ta.macd(df['Close']).fillna(0)
df['MACD_12_26_9'], df['MACDh_12_26_9'], df['MACDs_12_26_9'] = macd_vals.values.T

df['RSI_14'] = ta.rsi(df['Close']).fillna(0)

bbands = ta.bbands(df['Close']).fillna(0)
df = df.join(bbands)  # Gabungkan Bollinger Bands ke df

df['OBV'] = obv(df)  # Pastikan OBV tidak error
df['Date'] = pd.to_datetime(df['Date'])  # Pastikan kolom Date dalam format datetime

# Ambil daftar unik ticker
unique_tickers = df['Ticker'].unique()

# Sidebar
st.sidebar.title("Options")
selected_ticker = st.sidebar.selectbox("Select Ticker", unique_tickers)
chart_type = st.sidebar.selectbox("Select Chart Type", ["Candlestick", "Line Chart", "Bar Chart", "OHLC"])
indicator = st.sidebar.selectbox("Select Indicator", ["None", "MACD", "RSI", "Bollinger Bands", "OBV"])
time_range = st.sidebar.radio("Select Time Range", ["24h", "7w", "1mo", "1yr", "All"])

# Filter data berdasarkan ticker
df_ticker = df[df['Ticker'] == selected_ticker]

# Buat Figur
fig = go.Figure()

# Tambahkan Chart
if chart_type == "Candlestick":
    fig.add_trace(go.Candlestick(x=df_ticker['Date'], open=df_ticker['Open'], high=df_ticker['High'],
                                 low=df_ticker['Low'], close=df_ticker['Close'], name=f'Candlestick {selected_ticker}'))
elif chart_type == "Line Chart":
    fig.add_trace(go.Scatter(x=df_ticker['Date'], y=df_ticker['Close'], mode='lines', name=f'Line Chart {selected_ticker}'))
elif chart_type == "Bar Chart":
    fig.add_trace(go.Bar(x=df_ticker['Date'], y=df_ticker['Close'], name=f'Bar Chart {selected_ticker}'))
elif chart_type == "OHLC":
    fig.add_trace(go.Ohlc(x=df_ticker['Date'], open=df_ticker['Open'], high=df_ticker['High'],
                          low=df_ticker['Low'], close=df_ticker['Close'], name=f'OHLC {selected_ticker}'))

# Tambahkan Indikator
if indicator == "MACD":
    fig.add_trace(go.Scatter(x=df_ticker['Date'], y=df_ticker['MACD_12_26_9'], mode='lines', name='MACD'))
    fig.add_trace(go.Scatter(x=df_ticker['Date'], y=df_ticker['MACDs_12_26_9'], mode='lines', name='Signal Line'))
elif indicator == "RSI":
    fig.add_trace(go.Scatter(x=df_ticker['Date'], y=df_ticker['RSI_14'], mode='lines', name='RSI'))
elif indicator == "Bollinger Bands":
    fig.add_trace(go.Scatter(x=df_ticker['Date'], y=df_ticker['BBL_5_2.0'], mode='lines', name='Lower Band'))
    fig.add_trace(go.Scatter(x=df_ticker['Date'], y=df_ticker['BBU_5_2.0'], mode='lines', name='Upper Band'))
elif indicator == "OBV":
    fig.add_trace(go.Scatter(x=df_ticker['Date'], y=df_ticker['OBV'], mode='lines', name='OBV'))

# Atur Time Range
if time_range == "24h":
    fig.update_xaxes(range=[df_ticker['Date'].max() - pd.Timedelta(days=1), df_ticker['Date'].max()])
elif time_range == "7w":
    fig.update_xaxes(range=[df_ticker['Date'].max() - pd.Timedelta(weeks=7), df_ticker['Date'].max()])
elif time_range == "1mo":
    fig.update_xaxes(range=[df_ticker['Date'].max() - pd.DateOffset(months=1), df_ticker['Date'].max()])
elif time_range == "1yr":
    fig.update_xaxes(range=[df_ticker['Date'].max() - pd.DateOffset(years=1), df_ticker['Date'].max()])
else:
    fig.update_xaxes(range=[df_ticker['Date'].min(), df_ticker['Date'].max()])

# Update Layout
fig.update_layout(title="Crypto Price Visualization", xaxis_title="Date", yaxis_title="Price", xaxis_rangeslider_visible=True)

# Tampilkan Grafik
st.plotly_chart(fig)
