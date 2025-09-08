# QUESTION 1

import yfinance as yf

Tesla = yf.Ticker("TSLA")

tesla_data = Tesla.history(period="max")

tesla_data.head()
tesla_data.reset_index(inplace=True)

print(tesla_data)
