someInt = input()
someInt = int(someInt)

def digit(x,n):
  return ((x % (10 ** (n + 1))) - (x % (10 ** (n)))) // (10 ** n)

res = someInt
prev = -1
i = 0
while someInt != 0 and someInt != 1:
  if (res - someInt) // 10 == prev * someInt and digit(res,len(str(res)) - 1) == someInt:
    print (prev)
    break
  d = digit(res,i)
  i = i + 1
  prev = res
  res = res + d * someInt * (10 ** i)
else:
  print (someInt)