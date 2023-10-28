"""l"""

def triangle():
    """k"""
    anum = float(input())
    bnum = float(input())
    cnum = float(input())
    if (anum**2 + bnum**2) == cnum**2 or anum**2 + bnum**2 == cnum**2 + 0.01\
        or anum**2 + bnum**2 == cnum**2 - 0.01:
        print("Yes")
    elif (anum**2 + cnum**2) == bnum**2 or anum**2 + cnum**2 == bnum**2 + 0.01\
        or anum**2 + bnum**2 == cnum**2 - 0.01:
        print("Yes")
    elif (bnum**2 + cnum**2) == anum**2 or bnum**2 + cnum**2 == anum**2 + 0.01\
        or anum**2 + bnum**2 == cnum**2 - 0.01:
        print("Yes")
    else:
        print("No")
triangle()
