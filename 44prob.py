import numpy as np

# def isPentagonal(n):
# 	index = (1 + np.sqrt(1 + 24*n))/6
# 	if index == int(index):
# 		return True
# 	else:
# 		return False

def pentagonal(n):
	return n*(3*n  - 1) // 2

n = 2
D = 0
val = 0

pentagonals = []
for i in range(3000):
	pentagonals.append(pentagonal(n))

def isPentagonal(n):
	pents = set(pentagonals)
	if n in pents:
		return True
	return False

while n < 3000:
	num = pentagonals[n]
	for i in range(1, n-1):
		pent = pentagonals[n-1-i]
		if isPentagonal(num + pent) and isPentagonal(num - pent):
			val = num - pent
			break
	n += 1
print(val)
