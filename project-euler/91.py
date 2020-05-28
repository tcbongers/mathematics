class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def print(self):
		print(f'[{self.x}, {self.y}]')
		
def minus(a, b):
	return Vector(a.x - b.x, a.y - b.y)

def dot(a, b):
	return a.x*b.x + a.y*b.y
	
def is_right(P, Q):
	# Degenerate
	if P.x == 0 and P.y == 0:
		return 0
	if Q.x == 0 and Q.y == 0:
		return 0
	if P.x == Q.x and P.y == Q.y:
		return 0
		
	# Check whether the triangle with vertices at O, P, Q is right
	side1 = P
	side2 = Q
	side3 = minus(P, Q)
	
	if dot(side1, side2) == 0 or dot(side1, side3) == 0 or dot(side2, side3) == 0:
		return 1
		
	return 0
	
cap = 50	
count = 0

for x in range(0, cap + 1):
	for y in range(0, cap + 1):
		P = Vector(x, y)
		
		for a in range(0, cap + 1):
			for b in range(0, cap + 1):
				Q = Vector(a, b)
				
				if is_right(P, Q):
		#			P.print()
		#			Q.print()
		#			print("")
					count += 1
					
print(count // 2)