
word_file = open('p022_names.txt')
words = word_file.read()
words = words.replace('"', '')
words_list = words.split(",")
words_list.sort()

def word_score(word):
	word_vals = {
		"A":1,
		"B":2,
		"C":3,
		"D":4,
		"E":5,
		"F":6,
		"G":7,
		"H":8,
		"I":9,
		"J":10,
		"K":11,
		"L":12,
		"M":13,
		"N":14,
		"O":15,
		"P":16,
		"Q":17,
		"R":18,
		"S":19,
		"T":20,
		"U":21,
		"V":22,
		"W":23,
		"X":24,
		"Y":25,
		"Z":26
	}
	score = 0
	word = word.upper()
	for i in word:
		score += word_vals[i]
	return score

total = 0

for i in range(len(words_list)):
	total += (i+1)*word_score(words_list[i])

print(total)