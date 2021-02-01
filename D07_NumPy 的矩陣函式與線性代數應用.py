#作業目標：
#活用矩陣運算，實做線性代數
#作業重點：
#線性代數公式應用
#矩陣相乘維度需要對好，例如:2X3矩陣乘上3X5矩陣得到2X5矩陣

#題目:
#array1 = np.array([[10, 8], [3, 5]])

import numpy as np

#1. 運用上列array計算反矩陣，乘上原矩陣，並觀察是否為單位矩陣?
array1 = np.array([[10, 8], [3, 5]])
#反矩陣
array1_inverse = np.linalg.inv(array1)
print(array1_inverse)
#原矩陣乘上反矩陣
print(array1_inverse @ array1,"是單位矩陣")

#2. 運用上列array計算特徵值、特徵向量?
a = np.linalg.eig(array1)
print(a)

#3. 運用上列array計算SVD?
c = np.linalg.svd(array1)
print(c)
