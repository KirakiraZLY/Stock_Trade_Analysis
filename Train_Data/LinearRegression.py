import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
origDf = pd.read_csv('../Data_Loader/StockDir/桂东电力600310.ss.csv',encoding='utf-8')
df = origDf[['Close', 'High', 'Low','Open' ,'Volume']]
featureData = df[['Open', 'High', 'Volume','Low']]
feature = featureData.values
target = np.array(df['Close'])
#aiming at using open, high, low, volume to predict close
feature_train, feature_test, target_train ,target_test = train_test_split(feature,target,test_size=0.1)
predictedDays = int(math.ceil(0.1 * len(origDf)))
lrTool = LinearRegression()
lrTool.fit(feature_train,target_train)
predictByTest = lrTool.predict(feature_test)
index = 0
while index < len(origDf) - predictedDays:
    df.loc[index, 'predictedVal'] = origDf.loc[index, 'Close']
    df.loc[index, 'Date'] = origDf.loc[index, 'Date']
    index = index + 1
    predictedCnt = 0
while predictedCnt < predictedDays:
    df.loc[index, 'predictedVal'] = predictByTest[predictedCnt]
    df.loc[index, 'Date'] = origDf.loc[index, 'Date']
    predictedCnt = predictedCnt + 1
    index = index + 1

plt.figure()
df['predictedVal'].plot(color="red",label='predicted Data')
df['Close'].plot(color="blue",label='Real Data')
plt.legend(loc='best') # draw a legend
major_index = df.index[df.index % 10 == 0]
major_xtics = df['Date'][df.index % 10 == 0]
plt.xticks(major_index,major_xtics)
plt.setp(plt.gca().get_xticklabels(),rotation=30)
plt.grid(linestyle='-.')
plt.show()