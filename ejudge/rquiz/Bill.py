"""Bill"""

def billservicecharge(total):
    """calculation"""
    newtotal = 0
    if total * (10/100) <= 50:
        newtotal = total + 50
    elif total * (10/100) >= 1000:
        newtotal = total + 1000
    else:
        newtotal = total * (10/100) + total

    finaltotal = (newtotal * (7/100)) + newtotal
    print("%.2f" %finaltotal)
billservicecharge(int(input()))
