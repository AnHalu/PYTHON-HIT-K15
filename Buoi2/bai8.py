s = str(input())
total = s.count('1')
cnt = 0
if( total%2 ==0 ) :
    for i in range(len(s)):
        if (s[i] == '1'):
            cnt+=1
        if (cnt == total / 2):
            print(s[0:i+1],s[i+1:len(s)])
else : print('NO')
