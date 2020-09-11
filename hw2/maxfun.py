from sys import maxsize,stdin

def maxfun (s, *f):
	maxFunc = ""
	maxSum = -maxsize - 1
	for func in f:
		curSum = 0
		for n in s:
			curSum += func(n)
		if curSum >= maxSum:
			maxSum = curSum
			maxFunc = func
	return maxFunc

#inquery = stdin.readlines()
#for line in inquery:
#	eval(line)