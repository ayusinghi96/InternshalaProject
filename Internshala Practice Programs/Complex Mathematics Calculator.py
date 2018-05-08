import math
class Complex:
        
	def __init__(self, re=0, im=0):
		self.re = re
		self.im = im
		
	def __add__(self, n):
		return Complex(self.re + n.re, self.im + n.im)

	def __sub__(self, n):
		return Complex(self.re - n.re, self.im - n.im)

	def __mul__(self, n):
		real = (self.re*n.re - self.im*n.im)
		imag = (self.re*n.im + self.im*n.re)
		return Complex(real, imag)

	def __div__(self, n):
		real = (self.re*n.re + self.im*n.im)/(n.re**2 + n.im**2)
		imag = (self.im*n.re - self.re*n.im)/(n.re**2 + n.im**2)
		return Complex(real, imag)

	def __abs__(self):
		return (math.sqrt(self.re**2 + self.im**2))

	def __str__(self):

		if (self.im == 0):
			return ("%.2f" %(self.re))
		elif (self.re == 0):
			return ("%.2fi" %(self.im))
		else:
			if (self.im > 0):
				return ("%.2f + %.2fi" %(self.re, self.im))
			elif (self.im < 0):
				return ("%.2f - %.2fi" %(self.re, -1*self.im))

re_1 = float(input("Enter real part of first number : "))
img_1 = float(input("Enter imaginary part of first number : "))
re_2 = float(input("Enter real part of second number : "))
img_2 = float(input("Enter imaginary part of second number : "))

x = Complex(re_1, img_1)
y = Complex(re_2, img_2)

add = x + y
sub = x - y
mul = x * y
div = x.__div__(y)
modx = x.__abs__()
mody = y.__abs__()
print (add)
print (sub)
print (mul)
print (div)
print ("%.2f" %(modx))
print ("%.2f" %(mody))
