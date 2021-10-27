
aList = list(map(int , input().split()))
k = int (input())
ans = 0
for i in range(len(aList)) :
    ans += aList[i+1 : ].count(k-aList[i])

print(ans)




