import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

data = pd.read_csv("categorical_data.csv")
imp = SimpleImputer(missing_values=np.nan , strategy='mean')
data.iloc[:,1:3] = imp.fit_transform(data.iloc[:,1:3])
print("Sử dụng SimpleImputer :\n", data)
"""
imp tìm các thuộc tính missing là nan , sử dụng mean để tính giá trị trung bình
fit_tranform : thay các vị trí trùng với đièu kiện của imp thì thay vô 
"""

def caclMean(list) :
    sum = 0
    cnt = 0
    for i in list :
        if not np.isnan(i) :
            sum=sum+i
            cnt=cnt+1
    if cnt==0 : return None
    return sum/cnt

dataA = pd.read_csv('categorical_data.csv')
meanAge = caclMean(dataA.age)
meanSalary = caclMean(dataA.salary)
dataA['age'].fillna(value = meanAge, inplace = True )
dataA['salary'].fillna(value=meanSalary , inplace = True)
print("Tinh tay :\n " , dataA)
'''
tính giá trị mean của từng cột 
sau đó dùng fillna gán giá trị mean vào những NaN 
'''

