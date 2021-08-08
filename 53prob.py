


def factorials(n):
	vals = {}
	vals[0] = 1
	for i in range(1, n+1):
		vals[i] = i*vals[i-1]

	return vals

amt = 0

facts = factorials(101)

for i in range(23, 101):
	for r in range(4, i-3):
		val = (facts[i])/(facts[r]*facts[i-r])
		if val > 1000000:
			amt += 1

print(amt)