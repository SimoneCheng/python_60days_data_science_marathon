#作業目標：
#計算有缺失值的資料，統計量實作
#作業重點
#當遇到缺失值有函式可以處理，不須額外寫程式刪除
#計算統計量時不能出現缺失值

#題目:
#english_score = np.array([55,89,76,65,48,70])
#math_score = np.array([60,85,60,68,np.nan,60])
#chinese_score = np.array([65,90,82,72,66,77])
#上3列共六位同學的英文、數學、國文成績，第一個元素代表第一位同學，舉例第一位同學英文55分、數學60分、國文65分，
#今天第五位同學因某原因沒來考試，導致數學成績缺值，運用上列數據回答下列問題。

import numpy as np

english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,np.nan,60])
chinese_score = np.array([65,90,82,72,66,77])

#1. 請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略?
#各科平均
np.nanmean(english_score)
np.nanmean(math_score)
np.nanmean(chinese_score)
#各科最大值
np.nanmax(english_score)
np.nanmax(math_score)
np.nanmax(chinese_score)
#各科最小值
np.nanmin(english_score)
np.nanmin(math_score)
np.nanmin(chinese_score)
#各科標準差
np.nanstd(english_score)
np.nanstd(math_score)
np.nanstd(chinese_score)

#2. 第五位同學補考數學後成績為55，請計算補考後數學成績平均、最大值、最小值、標準差?
math_score[4] = 55
np.mean(math_score)
np.nanmax(math_score)
np.nanmin(math_score)
np.std(math_score)

#3. 用補考後資料找出與國文成績相關係數最高的學科?
corr_chi_math = np.corrcoef(chinese_score,math_score)
corr_chi_eng = np.corrcoef(chinese_score,english_score)
if corr_chi_math[0,1] > corr_chi_eng[0,1]:
    print("與國文成績相關係數最高的學科是數學")
elif corr_chi_math[0,1] == corr_chi_eng[0,1]:
    print("國文與數學的相關係數等於國文與英文的相關係數")
else:
    print("與國文成績相關係數最高的學科是英文")
