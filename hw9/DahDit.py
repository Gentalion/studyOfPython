class morse:
	def __init__(self):
		self.buf = ''
		self.dot = 'di'
		self.dash = 'dah'
		self.lastDot = 'dit'
		self.end = '.'
	
	def __init__(self, smth=''):
		self.buf = ''
		self.dot = 'di'
		self.dash = 'dah'
		self.lastDot = 'dit'
		self.end = '.'
		self.delimiter = True
		if len(smth) > 0:
			if smth.find(' ') > 0:
				smth = smth.split(' ')
			else:
				self.delimiter = False
				self.end = ''
				
			if len(smth) == 2:
				self.dot = smth[0]
				self.dash = smth[1]
				self.lastDot = smth[0]
			elif len(smth) > 2:
				self.dot = smth[0]
				self.lastDot = smth[1]
				self.dash = smth[2]
				if len(smth) > 3:
					self.end = smth[3]
		
		
	def __pos__ (self):
		self.buf = '.' + self.buf
		return self
	def __neg__ (self):
		self.buf = '-' + self.buf
		return self
	def __invert__ (self):
		self.buf = '!' + self.buf
		return self
	def __str__ (self):
		if len(self.buf) == 0:
			return self.end
		buf = self.buf + '!'
		isLastInWord = False
		res = ''
		for i in range(len(buf) - 1):
			if buf[i] == '-':
				if buf[i+1] == '!':
					res += ' ' * (0 if len(res) == 0 else 1) * (1 if self.delimiter else 0) + self.dash + ',' * (0 if i == len(buf) - 2 else 1) * (1 if self.delimiter else 0) + ' ' * (0 if i == len(buf) - 2 else 1) * (0 if self.delimiter else 1)
				else:
					res += ' ' * (0 if len(res) == 0 else 1) * (1 if self.delimiter else 0) + self.dash
			elif buf[i] == '.':
				if buf[i+1] == '!':
					res += ' ' * (0 if len(res) == 0 else 1) * (1 if self.delimiter else 0) + self.lastDot + ',' * (0 if i == len(buf) - 2 else 1) * (1 if self.delimiter else 0) + ' ' * (0 if i == len(buf) - 2 else 1) * (0 if self.delimiter else 1)
				else:
					res += ' ' * (0 if len(res) == 0 else 1) * (1 if self.delimiter else 0) + self.dot
		res += self.end
		
		return res