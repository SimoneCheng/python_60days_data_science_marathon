#作業目標：
#讀取存取陣列資料
#作業重點：
#多陣列存一起需要存成npz，讀取須注意npz中有多個陣列

import numpy as np

#. 將下兩列array存成npz檔
array1 = np.array(range(30))
array2 = np.array([2,3,5])
np.savez('file1.npz', array1=array1, array2=array2)

#2. 讀取剛剛的npz檔，加入下列array一起存成新的npz檔
a = np.load('file1.npz')
array3 = np.array([[4,5,6],[1,2,3]])
np.savez('file2.npz', a['arr_0'], a['arr_1'], array3)
