"""missingnumber"""
def missing(val):
    """function"""
    num = []
    for i in range(1, val):
        num.append(i)
    while True:
        given = int(input())
        if given == 0:
            break
        num.remove(given)
    for i in num:
        print(i)
missing(int(input()) + 1)
