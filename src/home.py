import streamlit as st
import pandas as pd
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
from datetime import datetime

def app():
    st.title('Stock Forecast App')
    st.sidebar.header('User Input Features')

    # Define prediction term options
    prediction_term = st.sidebar.radio(
        "Select Prediction Term:",
        ('Short-term', 'Medium-term', 'Long-term'),
        index=0  # Default to short-term
    )

    # Convert user selection into forecast period
    if prediction_term == 'Short-term':
        period = 30  # Approx. 1 month
    elif prediction_term == 'Medium-term':
        period = 180  # Approx. 6 months
    else:
        period = 365  # 1 year for long-term

    def load_data(ticker):
        start_date = '2010-01-01'
        end_date = datetime.now().strftime('%Y-%m-%d')
        data = yf.download(ticker, start=start_date, end=end_date)
        data.reset_index(inplace=True)
        return data

    def plot_raw_data(data):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
        fig.layout.update(title_text='Time Series Data', xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    # Plot raw data function remains unchanged

    ticker_list =  ['AAPL', 'TSLA', 'NVDA', 'PEP', 'AVGO', 'AZN', 'CSCO', 'ASML',
                'ADBE', 'TXN', 'AMGN', 'QCOM', 'INTC', 'SBUX', 'AMD', 'REGN',
                'MDLZ', 'VRTX', 'ISRG', 'PDD', 'ADI', 'ABNB', 'CHTR', 'AMAT',
                'MU', 'KDP', 'TEAM', 'MNST', 'ORLY', 'LRCX', 'SNPS', 'ADSK',
                'CDNS', 'CTAS', 'FTNT', 'BIIB', 'WDAY', 'DXCM', 'KLAC', 'LULU',
                'NXPI', 'CRWD', 'BIDU', 'ILMN', 'MRVL', 'CTSH', 'ODFL', 'ROST',
                'IDXX', 'CPRT', 'FAST', 'DDOG', 'SGEN', 'ZS', 'VRSN', 'ANSS',
                'ALGN', 'SWKS', 'DOCU', 'OKTA', 'ZM']

    st.title('Stock Forecast App')
    st.sidebar.header('User Input Features')



    # Define numeric inputs for detailed term selection
    if prediction_term == 'Short-term':
        days = st.sidebar.number_input('Number of days:', min_value=7, max_value=90, value=30)  # Default to 30 days
        period = days
    elif prediction_term == 'Medium-term':
        months = st.sidebar.number_input('Number of months:', min_value=1, max_value=24, value=6)  # Default to 6 months
        period = months * 30  # Approximate month to days conversion
    else:  # Long-term
        years = st.sidebar.number_input('Number of years:', min_value=1, max_value=10, value=1)  # Default to 1 year
        period = years * 365

    # Load data and plotting functions remain unchanged

    # Example ticker list and selection
    ticker_list = ['AAPL', 'TSLA', 'NVDA']  # Shortened for brevity
    selected_ticker = st.sidebar.selectbox('Select dataset for prediction', ticker_list)

    data_load_state = st.text('Loading data...')
    data = load_data(selected_ticker)
    data_load_state.text('Loading data... done!')

    st.subheader('Raw data')
    st.write(data.tail())

    plot_raw_data(data)

    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    st.subheader('Forecast data')
    st.write(forecast.tail())
        
    st.write(f'Forecast plot for {prediction_term.lower()}, {period} days')
    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)

    st.write("Forecast components")
    fig2 = m.plot_components(forecast)
    st.write(fig2)

# Don't forget to call the app function
if __name__ == "__main__":
    app()
