import pandas as pd
import pandas_datareader.data as web
from pandas_datareader.yahoo.headers import DEFAULT_HEADERS
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import requests_cache
import yfinance as yf

yf.pdr_override()


expire_after = dt.timedelta(days=3)
session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=expire_after)
session.headers = DEFAULT_HEADERS
start_date = dt.datetime(2023,1,1)
end_date = dt.datetime.today()

dolar = web.get_data_yahoo('USDBRL=X', start=start_date, end=end_date)
btc = web.get_data_yahoo('BTC-USD', start=start_date, end=end_date)

#print(dolar.head(10))


