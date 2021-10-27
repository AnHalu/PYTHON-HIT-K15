n = int(input())

ten = []
dantoc = []
for i in range(n) :
    x,y = map(str , input().split())
    ten.append([x,y])
    dantoc.append(y)
ten.sort(key=lambda x : dantoc.count(x[1]))
ans = [i[0] for i in ten if dantoc.count(i[1]) == dantoc.count(ten[-1][1])]
print(*ans , ' ')