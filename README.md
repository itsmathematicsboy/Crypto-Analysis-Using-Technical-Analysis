# Crypto Analysis Using Technical Analysis Dashboard

## Overview
Dashboard ini bertujuan untuk melakukan **analisis teknikal cryptocurrency** menggunakan data  
**OHLCV (Open, High, Low, Close, Volume)** yang diambil langsung dari **Yahoo Finance**  
melalui library `yfinance`.

Dashboard bersifat eksploratif dan informatif, **bukan sebagai rekomendasi investasi**.

---

## Assets Covered
Analisis dilakukan pada beberapa aset kripto dengan kapitalisasi besar dan likuiditas tinggi:

- Bitcoin (BTC)
- Ethereum (ETH)
- Tether (USDT)
- USD Coin (USDC)
- Solana (SOL)
- Cardano (ADA)
- Dogecoin (DOGE)
- TRON (TRX)
- Binance Coin (BNB)
- Ripple (XRP)

---

## Data Source
- **Provider**: Yahoo Finance  
- **Library**: `yfinance`  
- **Data Type**: OHLCV  
- **Frequency**: Daily (default Yahoo Finance)  
- **Date Range**: Variatif (menyesuaikan ketersediaan data)

Data diambil secara langsung tanpa menggunakan file CSV manual.

---

## Technical Indicators

### 1. Moving Average Convergence Divergence (MACD)
Digunakan untuk mengidentifikasi momentum dan arah tren harga:
- MACD Line
- Signal Line
- Histogram

### 2. Relative Strength Index (RSI)
Mengukur kondisi **overbought** dan **oversold**:
- Skala 0–100
- Level umum: 30 (oversold) dan 70 (overbought)

### 3. On-Balance Volume (OBV)
Digunakan untuk menganalisis hubungan antara pergerakan harga dan volume perdagangan.

### 4. Bollinger Bands (BB)
Digunakan untuk mengukur volatilitas harga:
- Upper Band
- Middle Band (Moving Average)
- Lower Band

---

## Time Range Configuration
Dashboard mendukung berbagai rentang waktu analisis sesuai ketersediaan data dari Yahoo Finance:

- Short-term: 1 bulan, 3 bulan
- Medium-term: 6 bulan, 1 tahun
- Long-term: 3 tahun, 5 tahun, Max

Pengguna dapat menyesuaikan time range untuk melihat perilaku indikator teknikal pada kondisi pasar yang berbeda.

---

## Visualization Components
Komponen visual utama dalam dashboard:

- Candlestick Chart (OHLC)
- Volume Chart
- MACD Panel
- RSI Panel
- OBV Line Chart
- Bollinger Bands Overlay

---

## Tools & Technology
- **Python**
- **yfinance** (data fetching)
- **pandas / numpy** (data processing)
- **matplotlib / plotly** (visualization)
- **Streamlit** (dashboard interface)

---

## Limitations
- Data bersifat historis, bukan real-time
- Tidak mempertimbangkan analisis fundamental atau sentimen pasar
- Stablecoin (USDT, USDC) memiliki volatilitas rendah sehingga indikator teknikal kurang signifikan

---

## Disclaimer
Dashboard ini dibuat untuk tujuan **edukasi dan eksplorasi data**.  
Semua analisis yang ditampilkan **bukan merupakan saran investasi**.
