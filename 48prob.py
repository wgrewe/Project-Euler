# Find last 10 digits of sum (n = 1 to 1000) n^n

# This sum is the same as mod 10,000,000,000 
# This is the same as sum (n = 1 to 1000) (n^n mod 10,000,000,000)

val = 0

for i in range(1,1001):
	amt = 1
	for j in range(i):
		amt *= i
		amt = amt % 10000000000
	val += amt 
	val = val % 10000000000

print(val)
