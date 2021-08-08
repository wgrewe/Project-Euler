# SOMETHING IS WRONG WITH THIS ONE

# Find the sum of all numbers which 
# cannot be written as the sum of 2 abundant numbers
# Note that all #'s > 28123 can be.

import numpy as np
import math

def getSumPropDivisors(n):
	sumDiv = 0
	if n == 1:
		return 0
	for i in range(2, int(math.floor(np.sqrt(n)))+1):
		if n%i == 0 and n//i != i:
			sumDiv += i + (n//i)
		elif n%i == 0:
			sumDiv += i
	return sumDiv +1

def isAbundant(n):
	if getSumPropDivisors(n) > n:
		return True
	else:
		return False

# def isSum(A, n):

# 	numDict = {}

# 	for i, e in enumerate(A):
# 		if n - e in numDict:
# 			return True
# 		numDict[e] = i
# 	return False

def isPair(arr, sum):
     
    # Create an empty hash set
    arr_size = len(arr)

    s = set()
     
    for i in range(0, arr_size):
        temp = sum-arr[i]
        if (temp in s):
            return True
        s.add(arr[i])
    return False
 

# def isSum(A, n):
# 	for i in A:
# 		for j in A:
# 			if i + j == n:
# 				return True
# 	return False		

abundantNums = []

sumAbun = 0

for i in range(1,28124):
	if isAbundant(i):
		abundantNums.append(i)
	if not isPair(abundantNums, i):
		sumAbun += i

print(sumAbun)

goal = 4179871



