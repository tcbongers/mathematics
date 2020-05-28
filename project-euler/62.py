cubes = [k**3 for k in range(100, 10000)]
cube_dict = {}
	
for k in range(100, 10000):
	c = k**3
	key = ''.join(sorted(str(c)))
	if key in cube_dict:
		cube_dict[key][0] += 1
		cube_dict[key].append(k)
	else:
		cube_dict[key] = [1, k]

for key in cube_dict:
	if cube_dict[key][0] == 5:
		print(cube_dict[key][1]**3)
		