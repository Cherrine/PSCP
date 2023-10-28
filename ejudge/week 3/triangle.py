"""l"""

def triangle():
    """k"""
    anum = float(input())
    bnum = float(input())
    cnum = float(input())
    tri1 = ((anum ** 2) + (bnum ** 2) - (cnum ** 2))
    tri2 = ((bnum ** 2) + (cnum ** 2) - (anum ** 2))
    tri3 = ((cnum ** 2) + (anum ** 2) - (bnum ** 2))
    if tri1 <= 0.01 and tri1 >= -0.01 or tri2 <= 0.01 and tri2 >= -0.01 \
        or tri3 <= 0.01 and tri3 >= -0.01:
        print("Yes")
    else:
        print("No")
triangle()
