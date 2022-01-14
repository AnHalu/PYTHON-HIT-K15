import numpy as np

a = np.random.randint(2,9,(3,3))
b = np.random.randint(10,20,(3,3))
c = a.dot(b)
print(c)

maxx = 0
tb = 0
for i in range(0,3) :
    for j in range(0,3) :
        tb =tb+ c[i][j]
        maxx = max(maxx,c[i][j])
print("Gia tri max :",maxx)
print("Gia tri trung binh : " ,tb/9)
