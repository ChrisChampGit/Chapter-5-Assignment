# QUESTION 1

import yfinance as yf

Tesla = yf.Ticker("TSLA")

tesla_data = Tesla.history(period="max")

tesla_data.head()
tesla_data.reset_index(inplace=True)

print(tesla_data)


# QUESTION 2

import pandas as pd
import requests
from bs4 import BeautifulSoup

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

html_data  = requests.get(url).text

soup = BeautifulSoup(html_data, 'html.parser')

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

table = soup.find_all("tbody")[1].find_all("tr")

for row in table:
    col = row.find_all("td")
    Date = col[0].text
    Revenue = col[1].text
  
    tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame({"Date":[Date], "Revenue":[Revenue]})], ignore_index=True)   
    tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"",regex=True) # Remove comma or dollar sign in Revenue Col
    tesla_revenue.dropna(inplace=True) # Remove null or empty strings on Rev Col
    tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

print(tesla_revenue.tail())


# QUESTION 3

import yfinance as yf

GameStop = yf.Ticker("GME")

gme_data = GameStop.history(period="max")

gme_data.head()
gme_data.reset_index(inplace=True)

print(gme_data)


# QUESTION 4

import pandas as pd
import requests
from bs4 import BeautifulSoup

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

html_data_2 = requests.get(url).text

soup = BeautifulSoup(html_data_2, 'html.parser')

gamestop_revenue = pd.DataFrame(columns=["Date", "Revenue"])

table = soup.find_all("tbody")[1].find_all("tr")

for row in table:
    col = row.find_all("td")
    Date = col[0].text
    Revenue = col[1].text

    gamestop_revenue = pd.concat([gamestop_revenue, pd.DataFrame({"Date":[Date], "Revenue":[Revenue]})], ignore_index=True)

print(gamestop_revenue.tail())

