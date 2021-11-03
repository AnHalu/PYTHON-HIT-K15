A = ('An', 'Binh', 'Nam', 'Long', 'Ngoc', 'Tu')
B = ('Binh', 'Linh', 'Nam', 'Hai', 'Long')
A = set(A)
B = set(B)
#a
A.remove('Tu')
print(A)
#b
A.add('Cuong')
print(A)
#c
C = A|B
print(C)
#d
D = A.intersection(B)
print(D)
#e
E = A - B
print(E)
#f
F = C - D
print(F)
#print(A)

