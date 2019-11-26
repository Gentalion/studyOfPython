def makeExpr (expr, firstArgExpand, secondArgExpand, thirdArgExpand):
	res = (' ' * (firstArgExpand - len(expr[0]))) + expr[0] + ' * '
	res += expr[1] + (' ' * (secondArgExpand - len(expr[1]))) + ' = '
	res += expr[2] + (' ' * (thirdArgExpand - len(expr[2])))
	return res

def makeColumnWithLength (a,n):
	pre = []
	
	firstArgLen = len(str(a))
	secondArgMaxLen = 0
	thirdArgMaxLen = 0
	for i in range(1,n+1):
		cur = (str(a), str(i), str(a * i))
		pre.append(cur)
		secondArgMaxLen = max(secondArgMaxLen, len(cur[1]))
		thirdArgMaxLen = max(thirdArgMaxLen, len(cur[2]))
	
	return (pre, firstArgLen, secondArgMaxLen, thirdArgMaxLen)

def concatColumns (columns, firstExpand, secondExpand, thirdExpand):
	res = []
	for row in columns[0]:
		res.append(makeExpr(row, firstExpand, secondExpand, thirdExpand))
	for col in columns[1:]:
		for row in range(len(col)):
			res[row] = res[row] + ' | ' + makeExpr(col[row], firstExpand, secondExpand, thirdExpand)
	
	return res

buf = input()
buf = buf.replace(',', ' ')
buf = buf.split()
n = int(buf[0])
m = int(buf[1])
delimiter = ''
for i in range(m):
	delimiter = delimiter + '='
print(delimiter)

toPrint = []
maxFirst, maxSecond, maxThird = 0, 0, 0
for i in range (1,n+1):
	cur,curFirst,curSecond,curThird = makeColumnWithLength(i,n)
	maxFirst = max(maxFirst, curFirst)
	maxSecond = max(maxSecond, curSecond)
	maxThird = max(maxThird, curThird)
	
	toPrint.append(cur)

colLength = maxFirst + maxSecond + maxThird + 6
colsInRow = -1
m += 3
while m > 0:
	m -= colLength + 3
	colsInRow += 1
for i in range (0,n,colsInRow):
	cur = concatColumns(toPrint[i:(i+colsInRow)],maxFirst,maxSecond,maxThird)
	for row in cur:
		print(row)
	print(delimiter)