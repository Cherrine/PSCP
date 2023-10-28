"""Niwarn World"""
import math
def xxx(nnn):
    """first func"""
    return 2 + ((math.log2(nnn**2)) / ((2*nnn) * math.log2(nnn)))
def yyy(nnn, sss):
    """sec func"""
    return (math.sin(math.radians(30)) + math.sqrt(2*sss)) / (xxx(nnn) + 3)
def zzz(kkk):
    """third func"""
    return (yyy(kkk, kkk)**2) + ((8456 * (xxx(kkk)**4)) / (24*kkk))

def main():
    """function"""
    nnn = float(input())
    sss = float(input())
    kkk = float(input())
    print("X: ""{0:.1f}"",".format(xxx(nnn)), "Y: ""{0:.1f}"",".format(yyy(nnn, sss)),\
       "Z: ""{0:.1f}".format(zzz(kkk)))
main()
