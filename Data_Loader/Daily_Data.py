import pandas as pd
import tushare as ts
import datetime
stock = ts.get_today_all()
stock.to_csv('today_stock_data.csv',encoding = 'utf-8',index=None)
stock_data = pd.read_csv('stock_data.csv',sep=',')
df = pd.concat([stock,stock_data])
df.to_csv('stock_data.csv',encoding = 'utf-8',index=None)