def fix (n):
	def take (f):
		def wrapper (*args, **kwargs):
			newArgs = []
			for cur in args:
				if type(cur) == float:
					cur = round(cur,n)
				newArgs.append(cur)
			newKwargs = {}
			for key,val in kwargs.items():
				if type(val) == float:
					val = round(val,n)
				newKwargs[key] = val
			buf = f(*newArgs, **newKwargs)
			if type(buf) == float:
				buf = round(buf,n)
			return buf
		return wrapper
	return take