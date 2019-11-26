image = {}
def draw (rect):
	rect = rect.split(' ')
	sizeX = int(rect[2])
	sizeY = int(rect[3])
	if sizeX == 0 or sizeY == 0:
		return (0,0,0,0)
	pointX = int(rect[0]) if sizeX > 0 else int(rect[0]) - 1
	pointY = int(rect[1]) if sizeY > 0 else int(rect[1]) - 1
	fillWith = rect[4]
	for x in range(pointX, pointX + sizeX, 1 if sizeX > 0 else -1):
		for y in range(pointY, pointY + sizeY, 1 if sizeY > 0 else -1):
			image[(x,y)] = fillWith
			#print('here')
	
	#print(image)
	return (min(pointX,pointX+sizeX-1 if sizeX > 0 else pointX+sizeX+1),
	        max(pointX,pointX+sizeX-1 if sizeX > 0 else pointX+sizeX+1),
			min(pointY,pointY+sizeY-1 if sizeY > 0 else pointY+sizeY+1),
			max(pointY,pointY+sizeY-1 if sizeY > 0 else pointY+sizeY+1))

buf = input()
bordersAny = False
borders = [] #minX,maxX,minY,maxY
while not buf.startswith('0 0 0 0'):
	buf = draw(buf)
	if not bordersAny:
		borders = list(buf)
		bordersAny = True
	else:
		borders[0] = min(borders[0],buf[0])
		borders[1] = max(borders[1],buf[1])
		borders[2] = min(borders[2],buf[2])
		borders[3] = max(borders[3],buf[3])
	
	buf = input()

#print(borders)
for y in range(borders[2], borders[3] + 1):
	buf = []
	for x in range(borders[0], borders[1] + 1):
		if not (x,y) in image:
			buf.append('.')
		else:
			buf.append(image[(x,y)])
	print(''.join(buf))
	
#print(image)