# Lexicographic 1000000th of 0123456789

def factorial(n):
	fact = 1
	if n <= 1:
		return fact
	for i in range(1,n+1):
		fact *= i
	return fact

digits = [0,1,2,3,4,5,6,7,8,9]
ordered = []

# start at 999999 for indexing
num = 999999

for i in range(10):
	completed = factorial(9-i)
	index = num//completed
	num = num - (index*completed)

	if i >=5:
		print(digits)
		print(completed)
		print(index)
		print(num)

	ordered.append(digits[index])
	digits.remove(digits[index])

	

print(ordered)

2783915460