作業目標：
熟悉陣列維度轉換，並且會擷取需要資料
作業重點：
使用reshape須注意order用法
where可以運用邏輯條件擷取資料

題目:
1.將下列陣列(array1)，轉成維度為(5X6)的array，順序按列填充。(hint:order="F")
2.呈上題的array，找出被6除餘1的數的索引

import numpy as np

#1.將下列清單(list1)，轉成維度為(5X6)的array，順序按列填充。(hint:order="F")
array1 = np.array(range(30))
array1.reshape((5,6),order = "F")

#2.解法一：呈上題的array，找出被6除餘1的數的索引（回傳的是值，不是索引）
for num in array1.flat:
    if num % 6 == 1:
        print(num)
        
#2.解法二：呈上題的array，找出被6除餘1的數的索引
np.argwhere(array1 % 6 == 1)
