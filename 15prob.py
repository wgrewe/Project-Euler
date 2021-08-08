# How many ways to traverse 20x20 grid from top left to bottom 
# right moving only down or right 

# This is equivalent to how many ways can you reorder 40 objects
# where there are 2 groups of 20 equivalent options

# This is a stars and bars argument

def factorial(n):
	val = 1
	if n < 0: 
		return None
	elif n == 0:
		return 1
	for i in range(1, n+1):
		val *= i
	return val


def choose(n,k):
	if n >= k:
		val = factorial(n) // (factorial(n-k)*factorial(k))
		return val
	else:
		return None

print(choose(40, 20))