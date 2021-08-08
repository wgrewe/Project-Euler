# a^b > c^d iff blog10(a) > dlog10(c)

import numpy as np 

number_file = open('p099_base_exp.txt')

max_base = 1
max_exp = 1
curr_line = 0

for i in range(1000):
	base_exp = number_file.readline()
	base_exp = base_exp.replace('\n', '')

	base_exp_list = list(map(int, base_exp.split(',')))
	base = base_exp_list[0]
	exp = base_exp_list[1]

	if base > max_base and exp > max_exp:
		max_base = base
		max_exp = exp
		curr_line = i

	elif exp*np.log(base) > max_exp*np.log(max_base):
		max_base = base
		max_exp = exp
		curr_line = i

print(max_base) 
print(max_exp)
print(curr_line)
