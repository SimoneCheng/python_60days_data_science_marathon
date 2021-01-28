#作業目標：
#讀取存取陣列資料
#作業重點：
#多陣列存一起需要存成npz，讀取須注意npz中有多個陣列

import numpy as np

#. 將下兩列array存成npz檔
array1 = np.array(range(30))
array2 = np.array([2,3,5])
with open('multi_array.npz', 'wb') as f:
    np.savez(f, array1=array1, array2=array2)

#2. 讀取剛剛的npz檔，加入下列array一起存成新的npz檔
a = np.load('multi_array.npz')
a.files
print(a['array1'])
print(a['array2'])
with open('multi_array.npz', 'wb') as f:
    np.savez(f, array1=array1, array2=array2, array3=array2)
