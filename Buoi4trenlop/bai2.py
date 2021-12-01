s = input()
if len(s)< 2 : s = ""
else :
    s = s[0]+s[1]+s[-2]+s[-1]
print(s)