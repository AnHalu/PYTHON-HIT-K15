a = list(map(lambda x: int(x[1]), input().split(',')))
even = list(filter(lambda x: x%2==0 , a))
odd = list(filter(lambda x: x%2!=0 , a))
print(tuple(even + odd))
