from vnstock import *
import calendar
import time
from datetime import datetime


# a= ticker_overview('TCB')
# print(a)

# df = stock_historical_data("GMD", "2022-12-01", "2022-12-14")
# print(df.head())

# df =  stock_intraday_data(symbol='GMD', page_num=0, page_size=5000)
# print(df.head())

# a = industry_analysis("VNM")
# a = market_top_mover('ForeignTrading')
# print(a)
c_time = datetime.now()
current_time = datetime.strftime(c_time, "%Y-%m-%d %H:%M:%S")

a = int(time.mktime(time.strptime(current_time,'%Y-%m-%d %H:%M:%S')))
# print(a)

b = api_get_foreign(a)
print(b)