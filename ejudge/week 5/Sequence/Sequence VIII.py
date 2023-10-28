"""sequence viii"""
def seq8(num):
    """calculate"""
    numset = num
    minus = num-1
    for _ in range(num):
        for row in range(num):
            if row+1 == numset:
                print('%02d'%(row+1-(minus)), end=' ')
                numset -= 1
                minus -= 1
            elif row+1 > numset:
                print('%02d'%(row+1-(minus+1)), end=' ')
            else:
                print('  ', end=' ')
        print('')
seq8(int(input()))