with open('p067_triangle.txt') as f:
# All the numbers in the file
	tree_val = f.read()

#splitting the number into a list
tree_val = tree_val.strip().split('\n')

#converting each and every list of strings to int
for i in range(0,len(tree_val)):
	tree_val[i] = tree_val[i].strip().split(' ')
	tree_val[i] = [int(x) for x in tree_val[i]]

for i in range(len(tree_val)-1, -1, -1):
	for j in range(i):
		tree_val[i-1][j] += max(tree_val[i][j], tree_val[i][j+1])

print(tree_val[0][0])
