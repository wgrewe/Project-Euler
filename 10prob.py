def isPrime(n):
	smallPrimes = [2,3,5,7,11,13,17,19]
	if n == 0 or n == 1:
		return False
	elif n in smallPrimes:
		return True
	elif n%2 == 0:
		return False
	else:
		d = 3
		while d*d <= n:
			if n % d == 0:
				return False
			d += 2
	return True

val = 0

for i in range(2000000):
	if isPrime(i):
		val += i
print(val)