def countdown(num):
	print("Start")
	while num > 0:
		yield num
		num -=1
val = countdown(5)

a = [1, 2, 3]
b = [i + 10 for i in a]
d = {i for i in range(11,15)}
e = (i for i in range(2, 8))
print(e)		