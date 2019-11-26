class WeAre:
	_count = 0
	def __init__ (self):
		WeAre._count += 1

	def __del__ (self):
		WeAre._count -= 1

	def getcount(self):
		return WeAre._count

	def setcount(self, value):
		pass

	def delcount(self):
		pass

	count = property(getcount, setcount, delcount, "i don't care")