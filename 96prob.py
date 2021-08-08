c = 28433
b = 7830457
num = 10000000000

digits = ((c*pow(2, b, mod = num)) +1) % num
print(digits)