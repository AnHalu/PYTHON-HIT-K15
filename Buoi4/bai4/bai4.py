s = input()
s.lower()
#a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z

def check() -> bool :
    for x in "abcdefghijklmnopqrstuvwxyz":
        if s.find(x)==-1 : return 0
    return 1
print(check() and "YES" or "NO" )