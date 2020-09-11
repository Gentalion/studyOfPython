def moar(a,b,n):
	countA = 0
	countB = 0
	for single in a:
		if single % n == 0:
			countA += 1
	
	for single in b:
		if single % n == 0:
			countB += 1
	
	return countA > countB