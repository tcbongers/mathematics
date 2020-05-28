with open('p022_names.txt', 'r') as f:
	lines = f.readlines()[0]
	names = [a[1:-1] for a in lines.split(',')]
	names.sort()
	
def namescore(name):
	return sum([ord(letter) + 1 - ord('A') for letter in name])
	
name_sum = 0

for row in range(len(names)):
	name_sum += (row + 1) * namescore(names[row])
	
print(name_sum)