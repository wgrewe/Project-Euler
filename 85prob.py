# Number of rectangles in lxw rectangle is sum_(1 <= x <= l, 1 <= y <= w) xy
# Closed form sum xy = (1/4)m(m+1)n(n+1)
# Product of two triangle numbers

import numpy as np 

def triangle(n):
	return n*(n+1)//2

close = 0
x = 0
y = 0

for m in range(1, 2003):
	tri_m = triangle(m)
	n_bound = 2*int((2100000//tri_m) ** (0.5))
	for n in range(1, n_bound):
		val = tri_m*triangle(n)
		if np.abs(2000000 - val) < np.abs(2000000 - close):
			x = m
			y = n
			close = val

print('x is: ', x)
print('y is: ', y)
print('Most rects are: ', close)
print('Area is: ', x*y)


