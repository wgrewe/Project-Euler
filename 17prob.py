# How many letters do you need to write out all numbers from 
# 1 to 1000

digits = {
	1:3,
	2:3,
	3:5,
	4:4,
	5:4,
	6:3,
	7:5,
	8:5,
	9:4}

teens = {	
	10:3,
	11:6,
	12:6,
	13:8,
	14:8,
	15:7,
	16:7,
	17:9,
	18:8,
	19:8
}

tens = {
	20:6,
	30:6,
	40:5,
	50:5,
	60:5,
	70:7,
	80:6,
	90:6
}

hundreds = {}
for i in digits.keys():
	hundreds[i] = digits[i]+10

digitSum = 0

single = 0
for i in digits:
	single += 90*digits[i]

seconds = 0
for i in tens:
	seconds += 100*tens[i]

teen = 0
for i in teens:
	teen += 10*teens[i]

hundred = 0
for i in hundreds:
	hundred += 100*hundreds[i] - 3

# include 1000
digitSum = single + seconds + teen + hundred
digitSum += 11
print(digitSum)


