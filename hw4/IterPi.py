def pigen():
    curAcc = 0
    curSign = -1.0
    curDivider = -1
    while True:
        curSign *= -1.0
        curDivider += 2
        curAcc += curSign * 4 / curDivider
        yield curAcc