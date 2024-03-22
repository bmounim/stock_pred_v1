# multi_stock_dashboard_with_plots.py
import streamlit as st
import yfinance as yf
import pandas as pd
def app() : 
        
    # Set the page configuration

    st.markdown("""
        <style>
        .big-font {
            font-size:30px !important;
            font-family: 'Comic Sans MS';
        }
        </style>
        """, unsafe_allow_html=True)


    # Dashboard title
    st.markdown("# 📈 Multi-Stock Dashboard with Visualizations")

    # Sidebar - Multi-select for choosing stocks
    st.sidebar.header('Select Stocks')
    selected_tickers = st.sidebar.multiselect('Tickers', [
        'AAPL', 'TSLA', 'NVDA', 'PEP', 'AVGO', 'AZN', 'CSCO', 'ASML',
        'ADBE', 'TXN', 'AMGN', 'QCOM', 'INTC', 'SBUX', 'AMD', 'REGN',
        'MDLZ', 'VRTX', 'ISRG', 'PDD', 'ADI', 'ABNB', 'CHTR', 'AMAT',
        'MU', 'KDP', 'TEAM', 'MNST', 'ORLY', 'LRCX', 'SNPS', 'ADSK',
        'CDNS', 'CTAS', 'FTNT', 'BIIB', 'WDAY', 'DXCM', 'KLAC', 'LULU',
        'NXPI', 'CRWD', 'BIDU', 'ILMN', 'MRVL', 'CTSH', 'ODFL', 'ROST',
        'IDXX', 'CPRT', 'FAST', 'DDOG', 'SGEN', 'ZS', 'VRSN', 'ANSS',
        'ALGN', 'SWKS', 'DOCU', 'OKTA', 'ZM'], default=['AAPL', 'TSLA'])

    st.sidebar.header("Select Period for Historical Data")
    period = st.sidebar.selectbox("Period",
                                options=["1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"],
                                index=3)

    # Function to fetch and cache historical stock data
    # Enhanced section for displaying additional company information
    def display_company_info(stock_info):
        st.subheader("Company Overview")
        try:
            # Basic Info
            company_name = stock_info.get('longName')
            website = stock_info.get('website')
            sector = stock_info.get('sector')
            industry = stock_info.get('industry')
            description = stock_info.get('longBusinessSummary')

            st.markdown(f"**Name:** {company_name}")
            st.markdown(f"**Website:** [Visit]({website})")
            st.markdown(f"**Sector:** {sector}")
            st.markdown(f"**Industry:** {industry}")
            st.markdown(f"**Description:** {description}")

            # Financial Health Indicators
            debt_to_equity = stock_info.get('debtToEquity', 'N/A')
            return_on_equity = stock_info.get('returnOnEquity', 'N/A')
            profit_margins = stock_info.get('profitMargins', 'N/A')
            st.markdown(f"**Debt to Equity:** {debt_to_equity}")
            st.markdown(f"**Return on Equity:** {return_on_equity}")
            st.markdown(f"**Profit Margins:** {profit_margins}")

            # Growth Metrics
            revenue_growth = stock_info.get('revenueGrowth', 'N/A')
            earnings_growth = stock_info.get('earningsGrowth', 'N/A')
            st.markdown(f"**Revenue Growth (YoY):** {revenue_growth}")
            st.markdown(f"**Earnings Growth (YoY):** {earnings_growth}")

        except ValueError:
            st.error("Failed to load company information.")
    def get_historical_data(ticker, period):
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)
        return hist

    # Example usage within the script for each selected ticker
    if selected_tickers:
        for ticker in selected_tickers:
            st.header(f"{ticker}")
            
            stock = yf.Ticker(ticker)
            stock_info = stock.info

            display_company_info(stock_info)
            
            # Fetch historical data for the ticker
            hist_data = get_historical_data(ticker,period)
            
            # Displaying historical closing price and volume charts...
            # (Your existing code for plotting goes here)




    # Displaying the data and plots
    if selected_tickers:
        for ticker in selected_tickers:
            st.header(f"{ticker}")
            
            # Fetch historical data for the ticker
            hist_data = get_historical_data(ticker, period)
            
            # Metrics and company info
            stock = yf.Ticker(ticker)
            info = stock.info
            col1, col2, col3 = st.columns(3)
            with col1:
                current_price = hist_data['Close'].iloc[-1]
                st.metric("Current Price", f"${current_price:.2f}")
                st.metric("Market Cap", f"${info.get('marketCap', 'N/A')}")
            with col2:
                st.metric("52-Week High", f"${info.get('fiftyTwoWeekHigh', 'N/A')}")
                st.metric("52-Week Low", f"${info.get('fiftyTwoWeekLow', 'N/A')}")
            with col3:
                st.metric("Beta", info.get('beta', 'N/A'))
            
            # Plotting historical closing price
            st.subheader("Historical Closing Price")
            st.line_chart(hist_data['Close'])
            st.metric(label="Latest Closing Price", value=hist_data['Close'].iloc[-1])

            # Plotting volume
            st.subheader("Trading Volume")
            st.bar_chart(hist_data['Volume'])

            st.markdown("---")
    else:
        st.error("Please select at least one stock to display.")

