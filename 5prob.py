# Find the smallest positive number divisible by all numbers from 
# 1 to 20

primes = {
	2:0,
	3:0,
	5:0,
	7:0,
	11:0,
	13:0,
	17:0,
	19:0
}

vals = list(range(21))

for i in range(21):
	num = vals[i]
	for j in primes.keys():
		divisor_num = 0
		while num % j == 0 and num > 1:
			divisor_num += 1
			num = num // j
			print(divisor_num)
		if divisor_num > primes[j]:
			primes[j] = divisor_num

prod = 1
for i in primes.keys():
	prod *= (i ** primes[i])

print(primes)
print(prod)






