import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests

def compile_data():
    with open("huStock.pickle", "rb") as f:
        tickets = pickle.load(f, encoding='gb2312')

    main_df = pd.DataFrame()
    for count, ticket in enumerate(tickets):
        arr = ticket.split('(')
        stock_name = arr[0]
        ticker = arr[1][:-1] + '.ss'
        df = pd.read_csv('StockDir/{}.csv'.format(stock_name+ticker))
        df.set_index('Date', inplace=True)

        df.rename(columns={'Adj Close': ticker}, inplace=True)
        df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')

        if count % 10 == 0:
            print(count)
        if count == 115: # cuz I just scraped 116 copies of data
            break
    print(main_df.head())
    main_df.to_csv('AShares_joined_closes.csv')
compile_data()