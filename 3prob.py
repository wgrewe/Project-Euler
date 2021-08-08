# Find largest prime factor of 600851475143
# Logic: Divisor may not always be prime, but since we clear out 
# the factors of divisor first, divisor will always be prime

num = 600851475143
divisor = 3
current_prime = 1

while num > 1:
	if num % divisor == 0:
		num  = num // divisor
		current_prime = divisor
	if num % divisor != 0 and num > 1:
		divisor += 2

print(divisor) 

