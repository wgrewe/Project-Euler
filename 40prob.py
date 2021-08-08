
n = 1
num = "0"
while len(num) < 1000001:
	sub = str(n)
	num += sub
	n += 1

print(num[:20])
val = 1
for i in range(1, 7):
	val *= int(num[10 ** i])
	print(num[10 ** i])

print(val)
