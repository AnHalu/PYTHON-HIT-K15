aList = list(map(int, input().split()))
result = []
sum = 0
for i in aList :
    sum += i
    result.append(sum)
print(result)