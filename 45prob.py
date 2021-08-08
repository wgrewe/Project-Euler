import numpy as np

# Logic: Every hex number is also triangular, so find next 
# hex number that is also pentagonal

nhex = 144
npent = 165
val = 1

def isPentagonal(n):
	index = (1 + np.sqrt(1 + 24*n))/6
	if index == int(index):
		return True
	else:
		return False

while val != 0:
	nexthex = nhex*(2*nhex - 1)
	if isPentagonal(nexthex):
		print(nexthex)
		break
	nhex += 1
			 

