# Longest Collatz sequence under 1,000,000

# Memory inefficient way

collatzLengthDict = {
	1:0
}

k = 1
while 2 ** k < 1000000:
	collatzLengthDict[2**k] = k
	k += 1

for i in range(3, 1000000):
	if i in collatzLengthDict.keys():
		continue
	cLen = 0
	val = i
	while val > 1:
		if val < i:
			cLen = cLen + collatzLengthDict[val]
			break
		elif val % 2 == 0:
			val = val // 2
			cLen += 1
		else:
			val = 3*val + 1
			cLen += 1
	collatzLengthDict[i] = cLen

print(max(collatzLengthDict, key=collatzLengthDict.get))
