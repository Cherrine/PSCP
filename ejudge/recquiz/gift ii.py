"""gift ii """
def gift():
    """gift list"""
    gift1 = int(input())
    gift2 = int(input())
    gift3 = int(input())
    gift4 = int(input())
    gift5 = int(input())
    gift6 = int(input())
    gift7 = int(input())
    gift8 = int(input())
    weightcheck(gift1)
    weightcheck(gift2)
    weightcheck(gift3)
    weightcheck(gift4)
    weightcheck(gift5)
    weightcheck(gift6)
    weightcheck(gift7)
    weightcheck(gift8)

def weightcheck(weight):
    """checking the weight"""
    if weight % 2 == 0:
        print(weight)

gift()
    