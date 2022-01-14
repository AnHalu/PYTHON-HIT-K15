import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np

data = pd.read_csv("data.csv")
imp = SimpleImputer(missing_values=np.nan , strategy='mean')
data.iloc[: , 1:3] = imp.fit_transform(data.iloc[: , 1:3])
Salary = data['Salary']
Coutry = data['Country']
id = Salary.argmax()
print("Max salary : " , Salary[id])
print("Coutry : " , Coutry[id] )

