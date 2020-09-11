from math import *

def substitute(func,x):
  return eval(func)

def f(x):
  return substitute(buf,x)

buf = input()
seg = input()
seg = seg.split(',')
curMin = float(seg[0])
curMax = float(seg[1])

dx = 1e-6
left = curMin
right = curMax
while abs(left - right) >= 1e-6:
  cur = (right - left) / 2 + left
  if f(cur) * f(left) > 0:
    left = cur
  else:
    right = cur

print (cur)