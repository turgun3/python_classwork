class Point(object):
	def __init__(self,point):
		self.point = point
	def show(self):
		print (self.point)	

class location(object):
	def __init__(self, x, y, z):
		self.coord = (x, y, z)

	def show(self):
		print (self.coord)

x = Point(10)
y = Point(20)
z = Point(30)
 
coord = location(x, y, z) 

x.show()
y.show()
z.show()

for x in coord.coord:
	x.show()