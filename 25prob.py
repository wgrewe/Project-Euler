# compute index of first fib with 1000 digits
# logic: use log10 to compute digits

import math

old2 = 1
old1 = 1
curr = 2
index = 3
digits = 1

while digits < 1000:
	index += 1
	old2 = old1
	old1 = curr
	curr = old1 + old2
	digits = math.floor(math.log10(curr)+1)

print(index)
