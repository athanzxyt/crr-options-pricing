import numpy as np
import requests
import yfinance as yf
import xml.etree.ElementTree as ET
from scipy.interpolate import interp1d

def calc_rf_rate():
    TREASURY_URL = "https://home.treasury.gov/sites/default/files/interest-rates/yield.xml"
    OVERNIGHT_RATE = 0
    FALLBACK_RISK_FREE_RATE = 0.02

    try:
        r = requests.get(TREASURY_URL)

        root = ET.fromstring(r.text)
        days = root.findall('.//G_BC_CAT')
        last = days[-1]

        def parse(node):
            return float(node.text)

        m1 = parse(last.find('BC_1MONTH'))
        m2 = parse(last.find('BC_2MONTH'))
        m3 = parse(last.find('BC_3MONTH'))
        m6 = parse(last.find('BC_6MONTH'))
        y1 = parse(last.find('BC_1YEAR'))
        y2 = parse(last.find('BC_2YEAR'))
        y3 = parse(last.find('BC_3YEAR'))
        y5 = parse(last.find('BC_5YEAR'))
        y7 = parse(last.find('BC_7YEAR'))
        y10 = parse(last.find('BC_10YEAR'))
        y20 = parse(last.find('BC_20YEAR'))
        y30 = parse(last.find('BC_30YEAR'))

        years = (0, 1/12, 2/12, 3/12, 6/12, 12/12, 24/12, 36/12, 60/12, 84/12, 120/12, 240/12, 360/12)
        rates = (OVERNIGHT_RATE, m1/100, m2/100, m3/100, m6/100, y1/100, y2/100, y3/100, y5/100, y7/100, y10/100, y20/100, y30/100)
        return interp1d(years, rates)
    
    except Exception:
        return lambda x: FALLBACK_RISK_FREE_RATE

def calc_sigma(ticker_symbol, period="5y"):
    stock_data = yf.download(ticker_symbol, period=period)
    log_returns = np.log(stock_data['Adj Close'] / stock_data['Adj Close'].shift(1))
    annualized_volatility = log_returns.std() * np.sqrt(252)  # Assuming 252 trading days in a year
    return annualized_volatility

def get_current_price(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    current_price = stock.history(period="1d")["Close"].iloc[0]
    return current_price

def get_options(ticker_symbol):
    pass