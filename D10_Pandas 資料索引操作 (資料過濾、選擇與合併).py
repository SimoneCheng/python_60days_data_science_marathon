#作業目標:
#運用索引找出需要資料
#合併資料的分法應用

#作業重點:
#分辨索引loc、iloc差別
#分辨合併資料方法的不同，因應不同情況使用Merge, join, concatenate

#題目:
#讀取STOCK_DAY_0050_202009.csv串聯STOCK_DAY_0050_202010.csv，並且找出open小於close的資料

import pandas as pd

#讀取STOCK_DAY_0050_202009.csv、STOCK_DAY_0050_202010.csv
stock_data1 = pd.read_csv('STOCK_DAY_0050_202009.csv')
stock_data2 = pd.read_csv('STOCK_DAY_0050_202010.csv')

#串聯
#用concat進行橫向的合併，axis = 0
stock_data3 = pd.concat([stock_data1,stock_data2],axis = 1)
stock_data3
#用concat進行縱向的合併，axis = 1
stock_data4 = pd.concat([stock_data1,stock_data2],axis = 0)
print(stock_data4)

#找出open小於close的資料
stock_data4.loc[stock_data4.open<stock_data4.close]
