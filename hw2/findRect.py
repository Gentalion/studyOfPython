field = [input()]

buf = '.'
while buf[0] != '-':
	buf = input()
	field.append(buf)
	pass

height = len(field)
width = len(field[0])

rectParts = {}
rectNumber = 0
for i in range(height):
	for j in range(width):
		if field[i][j] == '#':
			rectParts[(i,j)] = True
			if (i+1,j) in rectParts or (i-1,j) in rectParts or (i,j+1) in rectParts or (i,j-1) in rectParts:
				continue
			else:
				rectNumber += 1

print(rectNumber)