# Find the difference of (1 + 2 + ... + 100)^2 - (1^2 - 2^2 -...-100^2) 

def sum_first(n):
	return n*(n+1)/2

def square_sum_first(n):
	return n*(n+1)*(2*n+1)/6

print(sum_first(100) ** 2 - square_sum_first(100))