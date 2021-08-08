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

def isPerm(arr):
	val1 = sorted(str(arr[0]))
	for i in range(1,len(arr)):
		if val1 != sorted(str(arr[i])):
			return False
	return True


primeList = sieve(10000)
testPrimes = [x for x in primeList if x > 1000]

for i in primeList:
	
	length = (10000 - i) // 2

	for j in range(1, length):
		if (i + j) in primeList and (i + 2*j) in primeList:
			if isPerm([i, i+j, i+2*j]):
				print(i, i+j, i+2*j)

