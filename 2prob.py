# Find the sum of all even valued fibonacci numbers 
# less than 4 million

val = 0
old_fib = 1
fib_term = 1
new_fib_term = 2
while new_fib_term <= 4000000:
	if new_fib_term % 2 == 0:
		val += new_fib_term
	old_fib = fib_term
	fib_term = new_fib_term
	new_fib_term = old_fib + fib_term

print(val)