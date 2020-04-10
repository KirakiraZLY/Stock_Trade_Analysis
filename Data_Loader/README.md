#功能介绍
Daily_Data.py是利用pandas和tushare模块来爬取A股今日全部股票数据。
history_data.py是利用beautifulsoup来爬取全部股票历史数据的。
#使用方法
打开cmd  
`cd ./Data_Loader`  
`python Daily_Data.py`  
`python history_data.py`  
即可
#另外
我同时上传了一份A股三百多支股票2015/01/01至2020/03/24的交易数据，若只需要做简单的尝试可以直接使用这些数据。:)
#Feature
Run `Daily_Data.py` to scrap daily trade data from Chinese A share.   

Run `history_data.py`to scrap all history trade data from A share, where you can change start and end date.
#Quickstart
`cd ./Data_Loader`  
`python Daily_Data.py`  
`python history_data.py`
#Note
I have uploaded trade data of more than a hundred stocks from 2015/01/01 to 2020/03/24. If you just want to try some
 simple tasks, I warmly suggest you to use these data :)