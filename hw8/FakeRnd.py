class randintHelper:
	countRandIntCalls = 0
def randint(a,b):
	randintHelper.countRandIntCalls = (randintHelper.countRandIntCalls + 1) % 2
	if randintHelper.countRandIntCalls == 0:
		return b
	else:
		return a
class randrangeHelper:
	prevStart = -1
	newCur = -1
	prevEnd = -1
def randrange(a,b=False,c=False,d=False):
	if c != False:
		start = a
		end = b
		step = c
	elif b != False:
		start = a
		end = b
		step = 1
	else:
		start = 0
		end = a
		step = 1
	
	if start != randrangeHelper.prevStart or end != randrangeHelper.prevEnd:
		randrangeHelper.prevStart = start
		randrangeHelper.prevEnd = end
		randrangeHelper.newCur = start
	
	buf = randrangeHelper.newCur
	randrangeHelper.newCur += step
	if step > 0:
		if randrangeHelper.newCur >= end:
			randrangeHelper.newCur = randrangeHelper.newCur - end + start
	else:
		if randrangeHelper.newCur <= end:
			randrangeHelper.newCur = randrangeHelper.newCur - end + start
	
	return buf
		