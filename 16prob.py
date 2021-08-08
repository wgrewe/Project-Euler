# Sum digits of 2^1000

num = 2**1000
digitSum = 0
while num > 0:
	val = num % 10
	digitSum += val 
	num = num//10

print(digitSum)
