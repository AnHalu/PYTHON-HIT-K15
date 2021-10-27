#a
s = ""
while (len(s)<=10) :
    s = str(input("nhap chuoi : "))
print('Do dai cua chuoi la : ' , len(s))
print('Chuoi tu vi tri 2 den 6 : ' , s[2:7])
#b
s = s.lower()
print('Chuoi thuong ' , s)
s = s.upper()
print('Chuoi hoa : ' , s)

s = s.lower()
if('b' in s) :
    s = s.replace ('b' ,'g' )
print('Chuoi moi : ' , s)

#c
strr = 'hElLo-mY-NAMe-iS-SuZIe'
strr = strr.lower()
a = strr.split('-')
strr = ''

for i in a :
    i = i.capitalize()
    strr = strr + i + ' '
    #print(strr)
print("Y c : " , strr)

