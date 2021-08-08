

max_sols = 0
best_p = 0

for p in range(1001):
	num_sols = 0
	for a in range(p//2):
		b = (p*(p - 2*a))/(2*(p - a))
		if b == float(int(b)):
			num_sols += 1
	if num_sols > max_sols:
		max_sols = num_sols
		best_p = p

print('Max sols is ', max_sols, 'at p =', best_p)