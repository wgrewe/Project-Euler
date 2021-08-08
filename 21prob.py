import numpy as np

def getSumPropDivisors(n):
	sumDiv = 0
	for i in range(1, int(np.sqrt(n))+1):
		if n%i == 0 and n%i != i:
			sumDiv += i + (n//i)
		elif n%i == 0:
			sumDiv += i
	return sumDiv - n

sumDiv = np.zeros(10000)
for i in range(1,10000):
	sumDiv[i] = getSumPropDivisors(i)

sumAmicable = 0

for i in range(1,10000):
	j = sumDiv[i]
	if j != i and j < len(sumDiv) and sumDiv[int(j)] == i:
		sumAmicable += i

print(sumAmicable)

