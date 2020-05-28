digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def get_name(n):
	if n == 1000:
		return 'onethousand'

	if n >= 100:
		if n % 100 == 0:
			return digits[n//100] + 'hundred'
		
		return digits[n // 100] + 'hundredand' + get_name(n % 100)

	if n >= 20:
		return tens[n // 10] + get_name(n % 10)

	if n >= 10:
		return teens[n % 10]

	return digits[n]

#print(get_name(342))
#print(get_name(115))
#print(get_name(23))

count = 0
for k in range(1, 1001):
	#print(get_name(k))
	count += len(get_name(k))
	
print(count)