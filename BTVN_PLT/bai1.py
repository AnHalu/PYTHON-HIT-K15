import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('Mall_Customers_2.csv')
data.fillna(data['Age'].min(), inplace = True)
data = data.sort_values(by='Age')
fig , ax = plt.subplots(ncols=2, nrows=2, figsize = (15,15))
color = ['blue' if i == 'Male' else 'pink' for i in data['Genre']]
age = data['Age']
sp = data['Spending Score (1-100)']
for i in range(len(color)) :
    ax[0,0].scatter(age[i],sp[i],c= color[i])
ax[0,0].set(title='Scatter' , xlabel = 'Age' , ylabel = 'Spending Score (1-100)' )
'''
tao 1 mang color voi 2 gia tri blue for male or pink for female
ve scatter theo gia tri cua age (tuoi) , an (chi tieu ) 
'''

an = data['Annual Income (k$)']

ax[0,1].plot(age,an)
ax[0,1].set(title='Line' , xlabel='Age' , ylabel='Annual Income (k$)')
ax[0,1].annotate('Max' ,xy =(32 , 137) , xytext = (25,150) , arrowprops= dict(facecolor='green'))
'''
ham argamax() dua ra chi so ma thang data['Annual Income (k$)'] dat max 
ve plot nhu binh thuong 
tao mui ten bang annotate voi xy la toa do max ,xy =(age[id],an[id]) 
xytext la toa do cua chu thich mui ten xytext = (age[id]-10,an[id]+10)
arrowprops= dict(facecolor='green') -> tao mau cho mui ten 

'''
plt.show()


