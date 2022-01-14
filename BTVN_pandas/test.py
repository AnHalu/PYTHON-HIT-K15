import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

s1 = pd.Series([1,2,3,4])
s2 = pd.Series([5,6,7,8])
da = pd.concat([s1,s2])
print(da)