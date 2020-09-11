someInt = input()
digitsNum = len(someInt)
someInt = int(someInt)

if digitsNum == 1:
  print('YES')
elif someInt % 10 == 0:
  print('NO')
else:
  i = 0
  while i < digitsNum // 2:
    remain1 = ((someInt % (10 ** (i + 1))) - (someInt % (10 ** i))) / (10 ** i)
    remain2 = ((someInt % (10 ** (digitsNum - i))) - (someInt % (10 ** (digitsNum - i - 1)))) / (10 ** (digitsNum - i - 1))

    if remain1 == remain2:
      i = i + 1
      continue
    else:
      print('NO')
      break
  else:
    print('YES')