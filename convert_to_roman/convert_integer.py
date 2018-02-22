class ConvertInteger():
	"""class convert integer,has information on how 
	 to convert integer to roman 
	roman"""
	#intialize constructor 
	def __init__(self):
		#define digit mapping for roman
		self.romanMap=(('M',  1000),
                         ('CM', 900),
                         ('D',  500),
                         ('CD', 400),
                         ('C',  100),
                         ('XC', 90),
                         ('L',  50),
                         ('XL', 40),
                         ('X',  10),
                         ('IX', 9),
                         ('V',  5),
                         ('IV', 4),
                         ('I',  1))
	"""toRoman method take an integer and convert it to corresponing roman
	"""
	def toRoman(self,n):
		#check the range of integer given 
		"""convert integer to Roman numeral"""
		result=""
		for numeral,integer in self.romanMap:
			while n>=integer:
				result+=numeral
				n-=integer
		return result

#create instances of class convert integer 
a=ConvertInteger()
b=ConvertInteger()
print (a.toRoman(1423))
print (b.toRoman(1000))
