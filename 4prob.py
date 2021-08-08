# Find the largest palindrome that is a product of 2 3 digit numbers

from math import log10

large_pal = 0

# reverses a number

def rev(num):
    if num < 10:
        return num
    else:
        ones = num % 10
        rest = num // 10
        #print ones, rest, int(log10(rest) + 1), ones * 10 ** int(log10(rest) + 1)
        return ones * 10 ** int(log10(rest) + 1) + rev(rest)

# checks if palindrome

def is_pal(n):
	if n == rev(n):
		return True
	else:
		return False


for i in range(100,1000):
	for j in range(100,1000):
		val = i*j
		if is_pal(val):
			if val > large_pal:
				large_pal = val
print(large_pal)

