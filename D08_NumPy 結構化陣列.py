#作業目標：
#在一個陣列中放入多屬性陣列，進一步對陣列做運算
#作業重點：
#在建立結構化陣列前需要先設定屬性，在做運算時須注意資料屬性

import numpy as np 

name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]

#1. 將上列list依照['name', 'sex', 'weight', 'rank', 'myopia']順序擺入array，並且資料型態順序擺入[Unicode,Unicode,float,int,boolean]
dt = np.dtype('U4, U4, f, i, ?')
c = np.zeros(8, dtype = dt)
c['f0'] = name_list
c['f1'] = sex_list
c['f2'] = weight_list
c['f3'] = rank_list
c['f4'] = myopia_list
print(c)

#2. 呈上題，將array中體重(weight)數據集取出算出全部平均體重

#3. 呈上題，進一步算出男生(sex欄位是boy)平均體重

#4. 呈上題，進一步算出女生(sex欄位是girl)平均體重
