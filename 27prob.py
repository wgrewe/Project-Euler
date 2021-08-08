import numpy as np

# NOTE: Currently works but is inefficient
# Play around with selecting a, b
# Note if b = 2 then a even
# else a odd

A = range(-999,1001,2)

a = 1
b = 41
max_primes = 40

# GENERATE LIST OF PRIMES

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

primes = set(sieve(350000))

for i in A:
	ran_min = max(42, -1-i)
	b_list = list(set(range(ran_min, 998)) & primes)
	for k in b_list:
		val = 0
		for j in range(np.abs(k)+1):
			num = (j**2) + (i*j) + k
			num = int(num)
			if num in primes:
				val += 1
			else:
				break
		if val > max_primes:
			a = i
			b = k
			max_primes = val

print(a)
print(b)
print(max_primes)
print(a*b)