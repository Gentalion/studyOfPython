width,height = input().split(',')
width = int(width)
height = int(height)

curY = 0
curX = 0
delta = [(0,1), (1,0), (0,-1), (-1,0)]
curDelta = 0
curNumber = 0

field = {}
for i in range(width):
	field[(-1,i)] = -1
	field[(height,i)] = -1

for i in range(height):
	field[(i,-1)] = -1
	field[(i,width)] = -1

for i in range(width * height):
	#print(curY,' ',curX)
	field[(curY,curX)] = curNumber
	if (curY + delta[curDelta][0],curX + delta[curDelta][1]) in field:
		curDelta = (curDelta + 1) % 4

	curY += delta[curDelta][0]
	curX += delta[curDelta][1]
	curNumber = (curNumber + 1) % 10

#print(field)
fieldFixed = []
for i in range(height):
	buf = []
	for j in range(width):
		buf.append(str(field[(i,j)]))

	fieldFixed.append(' '.join(buf))

for i in range(height):
	print(fieldFixed[i])