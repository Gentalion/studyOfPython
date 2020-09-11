def mumboJumbo(lines):
	first = {}
	second = {}
	i = 0
	for line in lines:
		for char in line:
			if i == 0:
				first[char] = True
			elif i == 1:
				second[char] = True
		i = (i + 1) % 2
	
	return 'Mumbo' if len(first) > len(second) else 'Jumbo'
	
inquery = []
buf = ''
while True:
	buf = input()
	if buf == '':
		break
	else:
		inquery.append(buf)

print(mumboJumbo(inquery))