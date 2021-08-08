
word_file = open('p042_words.txt')
words = word_file.read()
words = words.replace('"', '')
words_list = words.split(",")

def get_triangles(n):
	triangles = []
	for i in range(1, n+1):
		triangles.append(i*(i+1)//2)
	return triangles


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

#Cap word score at 520 which is the score of Z*20
triangles = get_triangles(32)

for word in words_list:
	score = word_score(word)
	if score in triangles:
		total += 1

print(total)






