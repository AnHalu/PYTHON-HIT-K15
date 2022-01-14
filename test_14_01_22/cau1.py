aList = list(map(int, input().split()))
dict = {}
for x in range(aList[0] , aList[1]+1) :
    if x%aList[2] == 0 :
        dict[x] = x**2
print(dict)
