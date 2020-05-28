cap = 100000

tris = [(n*n + n) // 2 for n in range(cap)]
pents = [(3*n*n - n) // 2 for n in range(cap)]
hexs = [n*(2*n - 1) for n in range(cap)]
	
overlaps = set(tris) & set(pents) & set(hexs)
for o in overlaps:
	if o < 2:
		continue
		
	tri_ind = tris.index(o)
	pent_ind = pents.index(o)
	hexs_ind = hexs.index(o)
	
	print(f'T_{tri_ind} = P_{pent_ind} = H_{hexs_ind} = {o}')