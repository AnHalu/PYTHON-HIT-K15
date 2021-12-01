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
data1 = pd.read_csv("categorical_data.csv")
print("Tinh tay : ")
data1['age'].fillna(data1['age'].mean(),inplace = True)
print(data1)
data1['salary'].fillna(data1['salary'].mean(),inplace=True)
print(data1)
'''
data1['age'] /'salary' : lấy ra cột 'age' , 'salary' để thực hiện fillna()
Sử dụng phương thức fllna() để điền vào các dữ liệu bị thiếu , dùng mean() để 
tính gái trị trung bình , 
implace : true -> thay thế và sử dụng trực tiếp trên dataframe đang truy xuất đến 

'''





