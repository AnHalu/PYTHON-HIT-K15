import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
imp = SimpleImputer(missing_values=np.nan , strategy='mean')
data.iloc[: , 1:3] = imp.fit_transform(data.iloc[: , 1:3])

coun = data['Country'].values
age = data['Age'].values
sala = data['Salary'].values
pur = data['Purchased'].values

for i in set(coun) :
    for x in range(coun) :
        if(coun[x]==i) :
            plt.plot(age[x],sala[x])

plt.show()



