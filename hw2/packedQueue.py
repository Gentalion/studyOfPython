inquery = input()
start = 0
isTuple = False
tupleClosed = False
i = 0
buf = ''
archive = ()
while len(inquery) > 0 and i < len(inquery):
	#print (inquery[i])
	if inquery[i] == '(':
		isTuple = True
		tupleClosed = False
	elif inquery[i] == ')':
		tupleClosed = True
	elif inquery[i] == ',':
		if isTuple and not tupleClosed:
			i += 1
			continue
		else:
			#print('on start =',inquery[start])
			#print('on i =',inquery[i])
			buf = eval(inquery[start:i])
			#print(buf)
			inquery = inquery[i+1:]
			i = 0

			if isTuple:
				archive += buf
				#print('archive =',archive)
			else:
				#print('archive =',archive)
				if buf > len(archive):
					break
				print(archive[:buf])
				archive = archive[buf:]

			isTuple = False
			continue
	i += 1

