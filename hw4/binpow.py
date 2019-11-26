def BinPow (a, n, op):
    if n == 1:
        return a
    else:
        return op(BinPow(a,(n+1)//2,op),BinPow(a,n//2,op))
        