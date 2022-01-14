aList = list(map(int, input().split()))

aList = sorted(aList)
ans = []
for i in set(aList) :
    luu =[]
    for x in aList :
        if (x==i) :
            luu.append(i)
    ans.append(luu)
print(ans)