n = input()
list = list(map(int,input().split(" ")))
def cout(x) :
    cnt = 0
    for i in list :
        if x==i : cnt+=1
    return cnt

set = set(list)
for i in set :
    print(i , ":" , cout(i))
