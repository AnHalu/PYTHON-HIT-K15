

s = str(input())

kt = 0
a=0
for i in 'TRẺTRÂU' :
    check = s.find(i,a,len(s))
    if (check == -1) :
        kt=1
        break
    else :
        a=check +1

if (kt==1) :
    print('Không TRẺ TRÂU')
else :
    print('TRẺ TRÂU')
