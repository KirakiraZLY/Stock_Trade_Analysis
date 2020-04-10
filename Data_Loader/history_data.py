import bs4 as bs
import requests
import pickle
def GetHuStock():
    res = requests.get('https://www.banban.cn/gupiao/list_sh.html')
    res.encoding = res.apparent_encoding
    soup = bs.BeautifulSoup(res.text,'lxml')
    #从html内容中找到类名为'u-postcontent cz'的div标签
    content = soup.find('div',{'class':'u-postcontent cz'})
    result= []
    for item in content.findAll('a'):
        result.append(item.text)
    with open('huStock.pickle','wb') as f:
        pickle.dump(result,f)
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
from matplotlib import style
import matplotlib.pyplot as plt
import os
def GetStockFromYahoo(isHaveStockCode=False):
    if not isHaveStockCode:
        GetHuStock()
    with open('huStock.pickle', 'rb') as f:
        tickets = pickle.load(f, encoding='gb2312')
    if not os.path.exists('StockDir'):
        os.makedirs('StockDir')
    for ticket in tickets:
        arr = ticket.split('(')
        stock_name = arr[0]
        ticker = arr[1][:-1] + '.ss'
        if os.path.exists('StockDir/{}.csv'.format(stock_name + ticker)):
            print('{} Has Been Downloaded Yet'.format(stock_name+ticker))
        else:
            DownloadStock(stock_name, ticker)
            print('{} is downloading...'.format(stock_name+ticker))
def DownloadStock(stockName, stockCode):
    style.use('ggplot')
    start = dt.datetime(2015, 1, 1)
    end = dt.datetime(2020, 3, 24)
    # end = dt.datetime.now()
    # 根据股票代码从雅虎财经读取该股票在制定时间段的股票数据
    df = web.DataReader(stockCode, 'yahoo', start, end)
    # 保存为对应的文件
    df.to_csv('StockDir/{}.csv'.format(stockName + stockCode))
GetStockFromYahoo()

