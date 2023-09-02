import numpy as np
from scipy.stats import norm

def BlackScholes(type, S0, K, r, sigma, T):
    d1 = np.log(S0/K) + (r + sigma**2/2)*T / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    try:
        if type == "C":
            return S0 * norm.cdf(d1, 0 , 1) - K * np.exp(-r * T) * norm.cdf(d2, 0, 1)
        elif type == "P":
            return K * np.exp(-r * T) * norm.cdf(-d2, 0, 1) - S0 * norm.cdf(-d1, 0, 1)
    except:
        print("Please enter a valid option type: 'C' or 'P'")

    
