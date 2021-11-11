s = str(input())
a,b = s[s.index('(')+1 : s.index(')')].split(',')
print(a,b)