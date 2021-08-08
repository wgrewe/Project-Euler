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

def isPandigital(n):
	lst_n = [int(x) for x in str(n)]
	print(lst_n)
	if len(lst_n) == len(set(lst_n)) and len(lst_n) == max(lst_n):
		return True
	return False

# Sieve wor't run fast enough
# primes = set(sieve(1000000000))

# Idea: get an upper bound on pandigital primes

# 1 = 1
# 1 + 2 = 3
# ...
# 1 + 2 + ... + 9 = 

# sums = [1, 3, 6, 10, 15, 21, 28, 36, 45]

# A lot of these are divisible by 3, so the only primes can 
# be 4 or 7 digits

pandigital = 2143

for i in sieve(7654322):
	if isPandigital(i):
		pandigital = i

print(pandigital)



