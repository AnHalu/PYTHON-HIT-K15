aset = set(map(str, input().split()))
bset = set(map(str, input().split()))
check = bset - aset
if len(check) == 0 :
    print("la tap con")
else :
    print("ko la tap con")
