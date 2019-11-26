def statcounter ():
	stats = {}
	curf = yield stats
	while True:
		def send(f):
			def newfun (*args, **kwargs):
				if f in stats:
					stats[f] += 1
				else:
					stats[f] = 1
				return f(*args, **kwargs)
			return newfun
		curf = yield send(curf)