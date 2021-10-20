import math 

print('Nhap gia tri x :') 
x=(float)(input())
ans = (x*x + math.e**x + math.sin(x))/(math.sqrt(x*x+1)) 
print('Gia tri cua F(x) la : ' , ans ) 