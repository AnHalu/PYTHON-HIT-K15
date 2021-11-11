s = input()
ans = 0
for i in range(len(s)) :
    str = ""
    for j in range(i,len(s)) :

        str += s[j]
        if (len(str) > ans ) :
            if s.find(str,i+1 , len(s)) == -1 : break
            else : ans = len(str)
        #print(j, s[j], "chk" , ans )
    str = ""
print(ans)