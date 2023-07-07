import pandas as pd
import streamlit as st
import yfinance as yf
import datetime


st.write(
    """
        # Stock Price Analyser

        Shown are the stock prices  of MICROSOFT. 

"""
)

#ticker_symbol="MSFT"

ticker_symbol=st.text_input(
                            "enter the stock symbol",
                            "MSFT", 
                            key="placeholder"
)

col1,col2=st.columns(2)

with col1:
    start_date=st.date_input("enter the start date", 
                                
                                datetime.date(2019,1,1))

with col2:
    last_date=st.date_input("enter the last date", 
                        
                            datetime.date(2023,1,1))
    

st.write(
    """ 
        {ticker_symbol}'s EOD PRICE
"""
)

ticker_data=yf.Ticker(ticker_symbol)
ticker_df=ticker_data.history(period="1d",
                              start=f"{start_date}",           #formatting a date time object to string type
                              end=f"{last_date}")


st.dataframe(ticker_df)

st.write(
    """
        ## DAILY CLOSING CHART
"""
)

st.line_chart(ticker_df.Close)
 
st.write(
    """
        ## DAILY TRADED VOLUME CHART

"""
)
st.line_chart(ticker_df.Volume)

 