# -*- coding: utf-8 -*-
import pandas as pd
from sklearn import svm,preprocessing
import matplotlib.pyplot as plt

origDf = pd.read_csv('../Data_Loader/StockDir/保利地产600048.ss.csv', encoding = 'utf-8')
df = origDf[['Close', 'High', 'Low', 'Open', 'Volume', 'Date']]

df['diff'] = df['Close'] - df['Close'].shift(1)
df['diff'].fillna(0, inplace = True)

df['up'] = df['diff']
df['up'][df['diff']>0] = 1
df['up'][df['diff']<=0] = 0

df['predictForUp'] = 0

target = df['up']
length = len(df)
trainNum = int(length*0.8)
predictNum = length - trainNum

feature = df[['Close', 'High', 'Low', 'Open', 'Volume']]

feature = preprocessing.scale(feature)

featureTrain = feature[1:trainNum-1]
targetTrain = target[1:trainNum-1]
svmTool = svm.SVC(kernel = 'linear')
svmTool.fit(featureTrain, targetTrain)

predictedIndex = trainNum
while predictedIndex<length:
    testFeature = feature[predictedIndex:predictedIndex+1]
    predictForUp = svmTool.predict(testFeature)
    df.iat[predictedIndex, df.columns.get_loc('predictForUp')] = predictForUp#用loc改变不了
    predictedIndex = predictedIndex + 1

dfWithPredicted = df[trainNum:length]
print(dfWithPredicted['predictForUp'])

figure = plt.figure()

(axClose, axUpOrDown) = figure.subplots(2, sharex = True)
dfWithPredicted['Close'].plot(ax = axClose, color = 'pink')
dfWithPredicted['predictForUp'].plot(ax = axUpOrDown, color = 'red', label = 'Predicted Data')
dfWithPredicted['up'].plot(ax = axUpOrDown, color = 'blue', label = 'Real Data')
plt.legend(loc = 'best')

major_index = dfWithPredicted.index[dfWithPredicted.index % 15 == 0]
major_xtics = dfWithPredicted['Date'][dfWithPredicted.index % 15 == 0]
plt.xticks(major_index,major_xtics)
#plt.step(plt.gca().get_xticklabels(), rotation = 30)
plt.title('通过SVM预测保利地产的涨跌情况')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.show()