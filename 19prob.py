# How many sundays fell on the first of a month 
# between Jan 1 1901 and Dec 31 2000

# m = 1, t = 2, w = 3, h = 4, f = 5, s = 6, su = 7

# 52 weeks in 364 days, so if year starts on sunday  
# then there are 53 sundays. If leap year also fine to start on sat

month_days = {
	1:31,
	2:28,
	3:31,
	4:30,
	5:31,
	6:30,
	7:31,
	8:31,
	9:30,
	10:31,
	11:30,
	12:31
}

total_suns = 0

init_day = 366 % 7

for year in range(1901, 2001):
	for month in range(1,13):
		if init_day == 0:
			total_suns += 1
		
		init_day = init_day + month_days[month]
		if month == 2 and year % 4 == 0:
			init_day += 1
		init_day = init_day % 7

print(total_suns)







