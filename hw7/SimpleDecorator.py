def nonify (f):
	def newfun (*args, **kwds):
		buf = f(*args, **kwds)
		if buf != "" and buf != False:
			return buf
		else:
			return None
	return newfun