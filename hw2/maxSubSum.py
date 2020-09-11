from sys import maxsize
maxSubSum = -maxsize - 1
curSum = 0
while True:
	buf = int(input())
	if buf == 0:
		break
	else:
		curSum += int(buf)
		maxSubSum = maxSubSum if maxSubSum > curSum else curSum
		if curSum < 0:
			curSum = 0

print(maxSubSum)