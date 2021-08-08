def factorial(n):
	val = 1
	if n < 0: 
		return None
	elif n == 0:
		return 1
	for i in range(1, n+1):
		val *= i
	return val

num = factorial(100)
digitSum = 0
while num > 0:
	val = num % 10
	digitSum += val 
	num = num//10

print(digitSum)