import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Social_Network_Ads_2.csv')
data.rename(columns = {'Purchased' : 'Status'}, inplace=True)
data.fillna(data['EstimatedSalary'].min(), inplace= True)
change = ['Chua mua' if (i==0) else 'Da mua' for i in data['Status']]
data['Status'] = change
'''
dùng hàm rename đổi tên cột purchased thành satus 
dùng hàm fillna để xử lý missing data , thay thế nó bằng giá trị nhỏ nhất trong mảng
tạo 1 mảng change để lưu chuỗi chua mua hoặc đã mua dựa theo 0 hoặc 1 của data['status'] 
gán cột data['Status'] = change
'''
fig , ax = plt.subplots(ncols=2 , nrows=2 , figsize = (15,15))
age = data['Age']
est = data['EstimatedSalary']
colorA = ['red' if s == 'Chua mua' else 'green' for s in data['Status']]
for i in range(len(colorA)) :
    ax[0,0].bar(age[i],est[i], color = colorA[i])
ax[0,0].set(title = 'Bar Base on Age && Est' , xlabel = 'Age' , ylabel = 'EstimatedSalary')

colorB = ['violet' if s == 'Da mua' else 'red' for s in data['Status']]
for i in range(len(colorB)) :
    ax[0,1].scatter(age[i],est[i],c = colorB[i])
ax[0,1].set(title='Scatter Base on Age && Est ' , xlabel = 'Age' , ylabel = 'EstimatedSalary')

'''
tạo 1 mảng color nếu đã mua thì là violet chua mua thi la red duyet theo mang data['Status'] 
tạo mảng scatter theo 2 mang age và est như thường làm 
'''
plt.show()