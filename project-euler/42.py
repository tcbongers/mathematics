with open('p042_words.txt') as f:
	raw_words = f.readlines()[0].split(',')
	words = [w[1:-1] for w in raw_words]
	
tris = [n*(n - 1) // 2 for n in range(100)]
count = 0 

for w in words:
	if sum([ord(ch) - ord('A') + 1 for ch in w]) in tris:
		count += 1
		
print(count)