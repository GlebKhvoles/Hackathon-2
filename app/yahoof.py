import yfinance as yf

def fetchm_nq(ticker):
    nq = yf.Ticker(ticker)
    return nq.history(period="1y", interval="1d")