import numpy as np

def getNumDivisors(n):
	numDiv = 0
	for i in range(1, int(np.sqrt(n))+1):
		if n%i == 0 and n//i != i:
			numDiv += 2
		elif n%i == 0:
			numDiv += 1
	return numDiv

def getTriangleNum(n):
	return n*(n+1)//2

numDiv = 0
triNum = 50
while numDiv < 500:
	triNum += 1
	numDiv = getNumDivisors(getTriangleNum(triNum))
print(getTriangleNum(triNum))
