# PROBLEM 67

import math

# efficiently compute euler phi
# start with a sieve

def sieve(n):
	primeBool = [0]*(n+1)
	primeList = []

	for i in range(2, n+1):
		if primeBool[i] == 0:
			primeList.append(i)

			j = 2
			while (i*j <= n):
				primeBool[i*j] = 1
				j += 1
	return primeList

primes = sieve(1000001)

def eulerPhi(n):

	val = n

	i = 0
	while primes[i]**2 <= n:
		if n%primes[i] == 0:
			val -= n//primes[i]
			while n%primes[i] == 0:
				n = n//primes[i]
		i += 1
	if n>1:
		val -= val//n
	
	return val

# We can use the functions above but an analytical solution
# is much nicer. Some manipulation shows that we want 
# to maximize prod_{p|n} p/(p-1). p/(p-1) is a decreasing
# function, to maximize, we choose p as small as possible

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41]
n = 1
k = 0
while n*primes[k] <= 1000000:
	n *= primes[k]
	k += 1
print(n) 



