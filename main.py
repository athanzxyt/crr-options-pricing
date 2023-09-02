import crr
import black_scholes
from utils import *

def main():

    ticker = "AAPL"  
    ticker = input("Enter ticker symbol: ")

    current_price = get_current_price(ticker)
    print(f"\nCurrent Stock Price for {ticker}: ${current_price:.2f}")

    # risk_free_rate = 0.0544
    # risk_free_rate =  0.0412
    risk_free_rate = calc_rf_rate()
    print(f"\nRisk Free Rate: {risk_free_rate(8)}")

    sigma = calc_sigma(ticker, period='1y')
    print(f"\nAnnualized Volatility (Sigma) for {ticker}: {sigma:.4f}")

    # Calculate the option price using the Cox, Ross & Rubinstein (CRR) method
    option_price = black_scholes.BlackScholes("C", current_price, 335, risk_free_rate, sigma, 8/365)
    # option_price = crr.BinomialTreeCRR("C", current_price, 335, risk_free_rate, sigma, 8/365, american="true")
    print(f"\nOption Price for {ticker}: ${option_price:.2f}")

if __name__ == "__main__":
    main()
