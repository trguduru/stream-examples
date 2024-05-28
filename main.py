import streamlit as st
import yfinance as yf


st.title("Streamlit Stock Analysis App")

st.write("""

Shown are the stock closing price


""")


ticker = st.text_input("Enter the stock ticker:")
start_date = st.date_input("Select Start Date:")
end_date = st.date_input("Select End Date:")
tickerData = yf.Ticker(ticker)

tickerDataFrame = tickerData.history(period='id', start = start_date, end= end_date)

st.toggle("Activate")

numb_picked = st.slider("Pick a Number:",0,100)

st.write("Selected Number : ", numb_picked) 

st.line_chart(tickerDataFrame.Close)
st.line_chart(tickerDataFrame.Volume)

