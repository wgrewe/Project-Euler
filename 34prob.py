# Note that 9!x8 is a 7 digit number, so is 9!x7, thus we only need numbers up to 7 digits
# Moreover, 9!x7 = 2540160, so we only need numbers up to that.
# Factorial sum of 2540160 > 2540160 and factorial sum of 2540000 < 2540160
# Since the leading digit is at most a 2M, we can bound by 9!*6 + 2 = 

# Rules state single digit sums dont count

def digit_factorial_sum(n):
	factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

	val = 0

	while n > 0:
		last_digit = n % 10
		val += factorials[last_digit]
		n //= 10 

	return val

val = 0

for i in range(10, 2177283):
	if i == digit_factorial_sum(i):
		print(i)
		val += i

print('val is ', val)
