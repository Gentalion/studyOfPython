import math

someInt = input()
someInt = int(someInt)

maxI = int(math.sqrt(someInt)) + 1
i = 2
while i < maxI and i < 1001:
  j = i * i
  while j < someInt:
    j = j * i

  if j == someInt:
    print('YES')
    break
  else:
    i = i + 1
    continue

else:
  print('NO')
