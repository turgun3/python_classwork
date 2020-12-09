
while True:
	def calc(a, b, c):
		a = float(input("a = "))
		b = float(input("b = "))
		c = input ("Какое дейсвие выполнить (+,-,*,/): ")
		if c == '+':
			return a + b
		elif c == '-':
			return a - b
		elif c == '*':
			return a * b
		elif c == '/':
			return a / b
		else:
			break				