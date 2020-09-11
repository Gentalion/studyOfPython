class LetterAttr:

	def __init__(self):
		pass
	
	def __getattr__(self, name):
		if name in self.__dict__:
			return self.__dict__.get(name)
		else:
			return name
	
	def __setattr__(self,name,value):
		value = ''.join(filter(lambda x: x in name, value))
		self.__dict__[name] = value