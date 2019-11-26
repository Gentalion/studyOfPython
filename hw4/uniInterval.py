def length(a):
    return a[1] - a[0]

inquery = sorted(eval('[' + input() + ']'))

if len(inquery) == 0:
    print(0)
    exit()
    
countedTo = inquery[0][0]
result = 0

for cur in inquery:
    if cur[0] >= countedTo:
        result += length(cur)
    elif countedTo <= cur[1]:
        result += length((countedTo,cur[1]))
    countedTo = cur[1] if cur[1] > countedTo else countedTo

print(result)
    
    