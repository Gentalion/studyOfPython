def turtle (coord, direction):
	x,y = coord
	while True:
		inquery = yield (x,y)
		if inquery == 'f':
			if direction == 0:
				x += 1
			elif direction == 1:
				y += 1
			elif direction == 2:
				x -= 1
			elif direction == 3:
				y -= 1
		elif inquery == 'l':
			direction = (direction + 1) % 4
		elif inquery == 'r':
			direction = (direction - 1) % 4
