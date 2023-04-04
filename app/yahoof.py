import yfinance as yf

def fetchm_nq(ticker):
    nq = yf.Ticker(ticker)
    return nq.history(period="ytd", interval="1wk")