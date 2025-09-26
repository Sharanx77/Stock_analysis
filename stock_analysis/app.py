import streamlit as st
import yfinance as yf
import pandas as pd
import pandas_ta as ta
import plotly.graph_objects as go
from datetime import datetime

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="Stock Analysis Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Stock Analysis Dashboard")
st.caption(f"Analyze and visualize stock trends with key indicators. Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# --- Helper Functions ---
# Using st.cache_data to avoid re-downloading data on every interaction
@st.cache_data
def download_data(ticker, start_date, end_date):
    """Fetches stock data from Yahoo Finance and handles potential MultiIndex columns."""
    try:
        data = yf.download(ticker, start=start_date, end=end_date, progress=False)
        
        # FIX: The yfinance library can return a MultiIndex column structure.
        # pandas_ta expects a flat column structure. This checks for a MultiIndex
        # and flattens it if necessary, making the code more robust.
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.droplevel(1)
            
        return data
    except Exception as e:
        st.error(f"Failed to download data for {ticker}. Error: {e}")
        return None

@st.cache_data
def convert_df_to_csv(df):
    """Converts a DataFrame to a CSV string for download."""
    return df.to_csv(index=True).encode('utf-8')

# --- Sidebar for User Inputs ---
with st.sidebar:
    st.header("⚙️ Configuration")
    
    ticker = st.text_input("Enter Stock Ticker", value="AAPL").upper()
    start_date = st.date_input("Start Date", value=datetime(2023, 1, 1))
    end_date = st.date_input("End Date", value=datetime.now())

    st.subheader("Technical Indicators")
    short_ma = st.slider("Short-term SMA", min_value=5, max_value=50, value=20, step=1)
    long_ma = st.slider("Long-term SMA", min_value=50, max_value=200, value=50, step=1)
    ema_period = st.slider("EMA Period", min_value=5, max_value=50, value=20, step=1)
    rsi_period = st.slider("RSI Period", min_value=7, max_value=30, value=14, step=1)

    run_button = st.button("🚀 Run Analysis")

# --- Main Dashboard Area ---
if not run_button:
    st.info("Enter a stock ticker and click 'Run Analysis' in the sidebar to get started.")
else:
    if ticker:
        # 1. Fetch historical data
        data = download_data(ticker, start_date, end_date)

        if data is not None and not data.empty:
            # 2. Calculate technical indicators using pandas_ta
            # This library simplifies calculating indicators. It automatically appends columns to the DataFrame.
            data.ta.sma(length=short_ma, append=True)
            data.ta.sma(length=long_ma, append=True)
            data.ta.ema(length=ema_period, append=True)
            data.ta.rsi(length=rsi_period, append=True)
            data.dropna(inplace=True) # Remove rows with NaN values after calculations

            st.header(f"📊 Analysis for {ticker}")

            # 3. Plot candlestick and line graphs
            fig_price = go.Figure()

            # Candlestick chart for price
            fig_price.add_trace(go.Candlestick(x=data.index,
                                               open=data['Open'],
                                               high=data['High'],
                                               low=data['Low'],
                                               close=data['Close'],
                                               name='Price'))
            # Add Moving Averages (SMA and EMA)
            fig_price.add_trace(go.Scatter(x=data.index, y=data[f'SMA_{short_ma}'], mode='lines', name=f'{short_ma}-Period SMA', line=dict(color='orange', width=1.5)))
            fig_price.add_trace(go.Scatter(x=data.index, y=data[f'SMA_{long_ma}'], mode='lines', name=f'{long_ma}-Period SMA', line=dict(color='purple', width=1.5)))
            fig_price.add_trace(go.Scatter(x=data.index, y=data[f'EMA_{ema_period}'], mode='lines', name=f'{ema_period}-Period EMA', line=dict(color='cyan', width=1.5, dash='dash')))

            fig_price.update_layout(title=f'{ticker} Price with Moving Averages', yaxis_title='Price (USD)', xaxis_rangeslider_visible=False, legend=dict(x=0.01, y=0.99, traceorder='normal'))
            st.plotly_chart(fig_price, use_container_width=True)

            # RSI Plot
            fig_rsi = go.Figure()
            fig_rsi.add_trace(go.Scatter(x=data.index, y=data[f'RSI_{rsi_period}'], mode='lines', name='RSI', line=dict(color='lightgreen', width=2)))
            
            # Add overbought (70) and oversold (30) reference lines
            fig_rsi.add_hline(y=70, line_dash="dash", line_color="red", annotation_text="Overbought", annotation_position="bottom right")
            fig_rsi.add_hline(y=30, line_dash="dash", line_color="green", annotation_text="Oversold", annotation_position="top right")

            fig_rsi.update_layout(title=f'{ticker} Relative Strength Index (RSI)', yaxis_title='RSI Value', yaxis=dict(range=[0, 100]))
            st.plotly_chart(fig_rsi, use_container_width=True)

            # 4. Display performance summary
            st.header("📈 Performance Summary")
            start_price = data['Close'].iloc[0]
            end_price = data['Close'].iloc[-1]
            total_return = ((end_price / start_price) - 1)
            annualized_volatility = data['Close'].pct_change().std() * (252**0.5) # 252 trading days in a year
            
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Start Price", f"${start_price:,.2f}")
            col2.metric("End Price", f"${end_price:,.2f}")
            col3.metric("Total Return", f"{total_return:.2%}")
            col4.metric("Annualized Volatility", f"{annualized_volatility:.2%}")

            # 5. Display data table and add CSV export
            st.header("📄 Data and Export")
            st.dataframe(data.style.format("{:.2f}"))

            csv_data = convert_df_to_csv(data)
            st.download_button(
                label="📥 Download Data as CSV",
                data=csv_data,
                file_name=f'{ticker}_stock_data_{start_date}_to_{end_date}.csv',
                mime='text/csv',
            )
        else:
            st.error(f"Could not fetch data for '{ticker}'. Please check the ticker symbol and the selected date range.")
    else:
        st.warning("Please enter a stock ticker to begin the analysis.")
