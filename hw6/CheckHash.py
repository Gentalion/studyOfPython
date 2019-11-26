def checkhash(toHash, func, mod):
	dict = {}
	for i in toHash:
		cur = func(i) % mod
		if not cur in dict:
			dict[cur] = 1
		else:
			dict[cur] += 1
	collisions = []
	for i in dict.items():
		collisions.append(i[1])
	return (max(collisions), min(collisions))