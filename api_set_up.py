import yfinance as yf
import pprint

gme = yf.Ticker("GME")

pprint.pprint(gme.info) #gme.info is a dict
print(gme.info['open'])
price_points = ['open', 'close','dayHigh','dayLow']

hist = gme.history(period="2d")
print(type(hist))

pprint.pprint(hist[['Open', 'High', 'Close', 'Low']])