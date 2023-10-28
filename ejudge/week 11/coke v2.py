"""coke v2"""
def coke(price, cap, new, want):
    """function"""
    if cap == 0 or want == 0:
        print(price*want)
    elif new >= price:
        print(price*want)
    else:
        print((want*price)-(((want-1)//cap)*(price-new)))
coke(int(input()), int(input()), int(input()), int(input()))
