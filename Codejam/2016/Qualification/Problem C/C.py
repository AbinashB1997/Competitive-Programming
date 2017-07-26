from math import *
from fractions import *
from random import *

up = 20
bprimes = [1] * up
primes = [2]

tmp = 4
while tmp < up:
	bprimes[tmp] = 0
	tmp += 2

i = 3
while i < up:
	if bprimes[i]:
		primes.append(i)
		j = i + i
		while j < up:
			bprimes[j] = 0
			j += i
	i += 2
	
t = input()
n, J = [int(x) for x in raw_input().split()]


dic = {}

print "Case #1:"
cnt = 0
while cnt < J:
	s = bin(getrandbits(n-2))[2:]
	s = "0" * (n-2 - len(s)) + s
	s = "1" + s + "1"
	
	if s in dic: continue
	
	ints = [int(s, i) for i in xrange(2, 11)]
	
	divisors = []
	
	ok2 = True
	for i in ints:
		ok = False
		for p in primes:
			if i % p == 0:
				divisors.append(p)
				ok = True
				break
		if not ok:
			ok2 = False
			break
			
	if not ok2: continue
	
	print s,
	for div in divisors: print div,
	print
	
	cnt += 1
	dic[s] = 1
			
	
			
	
