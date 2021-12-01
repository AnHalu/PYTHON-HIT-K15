alist = list(map(int, input().split()))

ans = []
for i, j in enumerate(alist, 0):
    if j % 2 == 1:
        ans.append(i)
        alist.remove(j)

print(*ans, sep= ' ')
print(alist)