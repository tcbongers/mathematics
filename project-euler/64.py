"""
Library to handle continued fractions and the arithmetic involved.
"""

from fractions import Fraction
from math import sqrt

class Frac:
	"""
	Form a number of the form a + b sqrt(N) and do arithmetic operations on it.
	Assume that a and b are rational numbers implemented as fractions.Fraction
	
	Arguments: a, b, N
	
	Key methods: arithmetic operations and equality comparison.
	"""
	def __init__(self, a, b, N):
		self.a = a
		self.b = b
		self.N = N
		
	def __repr__(self):
		return f'{self.a} + {self.b} sqrt({self.N})'

	# Overload the standard arithmetic operations and equality
	def __add__(self, other):
		return Frac(self.a + other.a, self.b + other.b, self.N)

	def __sub__(self, other):
		return Frac(self.a - other.a, self.b - other.b, self.N)
		
	def __mul__(self, other):
		new_a = self.a*other.a + self.N*self.b*other.b
		new_b = self.a*other.b + self.b*other.a
		return Frac(new_a, new_b, self.N)
	
	def __truediv__(self, other):
		c = other.a
		d = other.b
		N = other.N
		
		inv = Frac(Fraction(c, c*c - d*d*N), Fraction(-d, c*c - d*d*N), N)
		return self*inv
		
	def __eq__(self, other):
		return self.a == other.a and self.b == other.b and self.N == other.N
		
	# Get the integer part; important for generating continued fractions
	def floor(self):
		return int(self.a + self.b*sqrt(self.N))
		
class ContinuedFraction:
	
	""" 
	Class to handle continued fractions.
	Store the data in an array; can print with nice formatting
	and reduce to a single fraction from the complex fraction form.
	"""
	
	def __init__(self, array, period=0, target_length=0):
		"""
		Store the fraction representation in an array
		Specify the period for a periodic continued fraction
		Target length is for when we want to specify how many
		terms appear in the ccontinued fraction
		"""
		
		self.array = array
		self.period = period
	
		# Handle periodic continuation
		if period > 0:
			periodic = array[-period:]
			while len(array) < target_length:
				self.array += periodic
			
		# Truncate to target length if specified
		if target_length > 0:
			self.array = self.array[:target_length]
			
	def __repr__(self):
		# Format nicely
		return '[' + str(self.array[0]) + ';' + ', '.join([str(_) for _ in self.array[1:]]) + ']'
		
	def reduce(self):
		# Reduce to a single rational number and return it
		array = self.array
		reduced = Fraction(array[-1], 1)
		for r in array[-2::-1]:
			reduced = Fraction(1, 1) / reduced + Fraction(r, 1)
			
		return reduced
		
def generateContinuedFraction(N, target_length = 0):
	"""
	Generate the continued fraction representation of N up to a specified target length
	If no target length is provided, keep going until we get periodicity.
	"""
	
	# Perfect square; terminate immediately
	if round(sqrt(N))**2 == N:
		return ContinuedFraction([N])
		
	# Store the remainders we've found to detect periodicity
	current_fraction = Frac(0, 1, N)
	remainders = [current_fraction]
	array = []
	
	while True:
		floor = current_fraction.floor()
		array.append(floor)
		current_fraction = Frac(1, 0, N) / (current_fraction - Frac(floor, 0, N))
		if current_fraction in remainders:
			break
		else:
			remainders.append(current_fraction)
	period = len(remainders) - remainders.index(current_fraction)

	return ContinuedFraction(array, period, target_length)
	
cap = 10000
count = 0

for n in range(cap + 1):
	cf = generateContinuedFraction(n)
	if cf.period % 2 == 1:
		print(n)
		count += 1
		
print(f'There are {count} odd-period continued fractions up to {cap}')