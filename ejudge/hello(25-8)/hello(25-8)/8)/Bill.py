"""Bill"""

def billservicecharge(total):
    newtotal = 0
    if total * (10/100) <= 50:
        newtotal = total + 50
    elif total * (10/100) >= 1000:
        newtotal = total + 1000
    else:
        newtotal = total * (10/100)
    print(newtotal)
    
billservicecharge(int(input()))
