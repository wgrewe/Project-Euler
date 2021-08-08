# Number of circular primes under 1,000,000

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

primes = set(sieve(1000000))


def isCircPrime(n):
	# give efficient check of circularity

	# If number contains 0,2,4,5,6,8 it is not a circular prime
	# Follows since one point is even or divisible by 5.
	# Thus 4^6 + 4^5 + ... + 4 = 5460 numbers to check

	notPrimeDigits = [0,2,4,5,6,8]
	check = n
	
	while check > 0:
		num = check%10
		if num in notPrimeDigits:
			return False
		check = check//10

	str_n = str(n)
	for i in range(len(str_n)):
		if n not in primes:
			return False
		new_string = str_n[-(i+1):] + str_n[:-(i+1)]
		n = int(new_string) 

	return True

	
# Start at 3 since 2,3,5 is a circ prime
numCirc = 3

# Range over odd to cut search space in 1/2

for i in range(7,1000000,2):
	if isCircPrime(i):
		numCirc += 1

print(numCirc)

