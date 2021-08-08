# Find the sum all multiples of 3 or 5 less than 1000

val = 0
for i in range(1000):
	if i % 15 == 0:
		val += i
	elif i % 5 == 0:
		val += i
	elif i % 3 == 0:
		val += i

print(val)