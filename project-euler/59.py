from itertools import product
from string import ascii_lowercase as low

def decrypt(code, password):
	clear = ''
	for i in range(len(code)):
		clear += chr(code[i]^ord(password[i%len(password)]))
	return clear
	
with open('p059_cipher.txt') as f:
	code = [int(_) for _ in f.read().split(',')]

#print(code)
count = 0
#for password in product(low, repeat=3):
#	clear = decrypt(code, password)
#	if 'the ' in clear:
#		count += 1
#		pw = ''.join(password)
#		print(f'Potential password: {pw}')
		
#print(f'{count} candidates')

#pw = ['adp', 'drp', 'eug', 'euq', 'exp', 'hop']
#for p in pw:
#	print(decrypt(code, p))

clear = decrypt(code, 'exp')
print(clear)
ascii_sum = sum([ord(_) for _ in clear])
print(f'Ascii sum = {ascii_sum}')