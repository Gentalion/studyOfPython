routes={}
buf = input().split(' ')
while len(buf) == 2:
	if buf[0] in routes:
		if routes[buf[0]].find(buf[1]) < 0:
			routes[buf[0]] = routes[buf[0]] + ' ' + buf[1]
	else:
		routes[buf[0]] = buf[1]
	if buf[1] in routes:
		if routes[buf[1]].find(buf[0]) < 0:
			routes[buf[1]] = routes[buf[1]] + ' ' + buf[0]
	else:
		routes[buf[1]] = buf[0]
	buf = input().split(' ')
pointFrom = buf[0]
pointTo = input()

routesCur = {}
routesCur[pointFrom] = True
routesPrev = {}
foundRout = False
if pointFrom in routes and pointFrom in routes:
	while routesPrev != routesCur and not foundRout:
		routesPrev = routesCur
		routesCur = {}
		
		for fromPrev in routesPrev.items():
			routesCur[fromPrev[0]] = True
			for elem in (routes[fromPrev[0]].split(' ')):
				if elem == pointTo:
					foundRout = True
				else:
					routesCur[elem] = True

if foundRout:
	print('YES')
else:
	print('NO')

