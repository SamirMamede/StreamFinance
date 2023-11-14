import pandas as pd
import pandas_datareader.data as web
from pandas_datareader.yahoo.headers import DEFAULT_HEADERS
import datetime as dt
import requests_cache


start_date = dt.datetime(2023,1,1)
end_date = dt.datetime.today()

df = web.get_data_fred('GS10', start=start_date, end=end_date)
print(df.head(10))