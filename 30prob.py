# Find the sum of all numbers that can be written
# as the fifth power of their digits

# The trick is to find the upper bound, note that 9^5 is 
# about 32000, so for 6 digit numbers we have an upper bound of 
# exactly 354,294. Thus, we cannot have a number larger than that.
# We have similar problems for all other numbers

def isSum(n):
	
	# check = n
	# while check > 0:
	# 	num = check%10
	# 	if num in notGood:
	# 		return False
	# 	check = check//10

	powers = [0,1,32,243,1024,3125,7776,16807,32768,59049]

	str_n = str(n)
	val = 0
	for i in str_n:
		ival = int(i)
		val += powers[ival]

	if val == n:
		return True

sumVal = 0
for i in range(2, 354294):
	if isSum(i):
		sumVal += i

print(sumVal)

