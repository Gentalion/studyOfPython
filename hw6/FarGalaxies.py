def distance (a, b):
	return (abs(a[0] - b[0]) ** 2) + (abs(a[1] - b[1]) ** 2) + (abs(a[2] - b[2]) ** 2)

galaxies = []

buf = input().split(' ')
i = 0
maxDistance = -1
firstGalaxy = ''
secondGalaxy = ''
while len(buf) == 4:
	i += 1
	newGalaxy = (float(buf[0]),float(buf[1]),float(buf[2]),buf[3])
	
	for galaxy in galaxies:
		newDistance = distance(newGalaxy, galaxy)
		if newDistance > maxDistance:
			maxDistance = newDistance
			firstGalaxy = galaxy[3]
			secondGalaxy = newGalaxy[3]
		
	galaxies.append(newGalaxy)
	buf = input().split(' ')

if maxDistance == -1 or maxDistance == 0:
	print(galaxies[0][3] + ' ' + galaxies[0][3])
else:
	print(min(firstGalaxy,secondGalaxy) + ' ' + max(firstGalaxy,secondGalaxy))
		