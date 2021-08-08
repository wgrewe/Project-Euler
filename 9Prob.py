# There is one pythag triplet (a,b,c) with a+b+c=1000
# Return abc

for a in range(1,500):
	for b in range(a):
		c = 1000 - a - b
		if (a**2 + b**2) == c**2:
			print(a, b, c)
			print('val is', a*b*c)