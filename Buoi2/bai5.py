n = int(input())
res = 0
while (n>=10) :
    while(n>0) :
        res += n%10
        n//=10
        #print(res,' ', n)
    n = res
    res = 0

print(n)