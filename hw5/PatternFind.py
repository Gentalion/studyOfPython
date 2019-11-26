buf = input()
template = input()
templateRemastered = []
previousWatch = 0
watch = template.find('@')
while watch != -1:
	if watch != previousWatch:
		templateRemastered.append(template[previousWatch:watch])
	templateRemastered.append('')
	
	previousWatch = watch + 1
	watch = template.find('@', previousWatch)
templateRemastered.append(template[previousWatch:])

template = templateRemastered
#print(template)

watch = 0
anotherRemember = 0
while len(template) > 0:
	if template[0] == '':
		template = template[1:]
		anotherRemember += 1
	else:
		break

if len(template) == 1:
	print(buf.find(template[0]) - anotherRemember)
elif len(template) == 0:
	print(0)
else:
	watch = buf.find(template[0], watch)
	foundSmth = False
	while watch > 0:
		#print(buf[watch:])
		rememberWatch = watch
		watch += len(template[0])
		okSoFar = True
		for i in range(1,len(template)):
			if template[i] == '':
				watch += 1
				#print(buf[watch:])
			else:
				if not buf[watch:].startswith(template[i]):
					okSoFar = False
					break
				else:
					watch += len(template[i])
					#print(buf[watch:])
		if okSoFar:
			print(rememberWatch - anotherRemember)
			foundSmth = True
			break
		watch = buf.find(template[0], rememberWatch + 1)
		#print('')

	if not foundSmth:
		print(-1)

		