from operator import itemgetter
def shex(n): # переводит число n в 64-ричное представление
	res = ''
	while n > 0:
		cur = n % 64
		res = chr(cur + 32) + res
		n -= cur
		n = int(n / 64)
	return res

def xehs(s): # переводит число в 64-ричном представлении в обычное число
	res = 0
	for i in s:
		res *= 64
		res += ord(i) - 32
	return res

def string2bits(s, offset=0, length=8):
    return [bin(ord(x)-offset)[2:].zfill(length) for x in s]

def bits2string(b, offset=0):
    return ''.join([chr(int(x, 2) + offset) for x in b])
	
def longBitStringToBites (bs): # дописывает нули в конце
	cur = ''
	res = []
	for symbol in bs:
		cur += symbol
		if len(cur) == 6:
			res.append(cur)
			cur = ''
	
	if len(cur) > 0:
		cur += '0' * (6 - len(cur))
		res.append(cur)
	
	return res

def encode (txt):
	stat = {}
	for i in txt:
		if i in stat:
			stat[i] += 1
		else:
			stat[i] = 1
	
	encoding = {}
	curEncodingSymbol = '0'
	while len(stat) > 0:
		maxOccur = -1
		whoIsMaxOccur = chr(0)
		for key,val in stat.items():
			if val > maxOccur:
				maxOccur = val
				whoIsMaxOccur = key
			elif val == maxOccur:
				if key > whoIsMaxOccur:
					whoIsMaxOccur = key
		stat.pop(whoIsMaxOccur)
		encoding[whoIsMaxOccur] = curEncodingSymbol
		curEncodingSymbol = '1' + curEncodingSymbol
	txtBits = ''
	for symbol in txt:
		txtBits += encoding[symbol]
	return(len(txt),''.join(map(itemgetter(0), encoding.items())), bits2string(longBitStringToBites(txtBits),32))
	
def decode (txtLen, table, code):
	encoding = {}
	curEncodingSymbol = '0'
	for symbol in table:
		encoding[curEncodingSymbol] = symbol
		curEncodingSymbol = '1' + curEncodingSymbol
	
	buf = ''
	res=''
	for bit in ''.join(string2bits(code,32,6)):
		buf += bit
		if bit == '0':
			res += encoding[buf]
			buf = ''
			if len(res) >= txtLen:
				break
	
	return res

#print(xehs("BREAKFAST"))
#print(shex(10844745761445995))
#res = encode("ENGINEERING WITHOUT MANAGEMENT IS ART.")
#print(res)
#txt = decode(*res)
#print(txt)