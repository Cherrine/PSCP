"""longer"""
import math
def long(rnum, anum, bnum):
    """function"""
    circle = 2 * math.pi * rnum
    rec = 2 * (anum + bnum)
    recans = rec - circle
    cirans = circle - rec
    if circle > rec:
        print("Circle is longer")
        print("%.5f" %cirans)

    elif circle < rec:
        print("Rectangle is longer")
        print("%.5f" %recans)

    elif circle == rec:
        print("Equal")
        print("%.5f" %circle)

long(float(input()), float(input()), float(input()))
