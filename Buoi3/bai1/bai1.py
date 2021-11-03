alist = list(map(int,input().split()))
ans =[]

def xd10() :
    for i in alist :
        a = str(i)
        if ('1' in a) :
            ans.append(i)
            continue
        if ('0' in a) :
            ans.append(i)
            continue
xd10()
def ss10() :
    check = []
    for i in ans :
        list = []
        a = str(i)
        for i in range(0,len(a)) :
            if(a[i] =='0' or a[i]=='1') :
                list.append(i)
        check.append(list)

    for i in range(0,len(check)) :
        for j in range(i+1,len(check)) :
            if(check[i] == check[j]) :
                check[j] =[]
    for i in range(0,len(check)) :
        if len(check[i])!=0 :
            print(ans[i])
ss10()


