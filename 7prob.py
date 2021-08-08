# What is the 10001st prime number

def isPrime(n):
	if n == 0 or n == 1:
		return False
	elif n == 2:
		return True
	else:
		d = 3
		while d*d <= n:
			if n % d == 0:
				return False
			d += 2
	return True

num_prime = 1
val = 3

while num_prime < 10001:
	if isPrime(val):
		num_prime += 1
		if num_prime == 10001:
			print(val)
	val += 2