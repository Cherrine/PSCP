"""tax"""
def tax(year, engine):
    """discount check"""
    result = enginecheck(engine)
    if year > 5:
        if year == 6:
            result = result - (result * 0.1)
        elif year == 7:
            result = result - (result * 0.2)
        elif year == 8:
            result = result - (result * 0.3)
        elif year == 9:
            result = result - (result * 0.4)
        elif year >= 10:
            result = result - (result * 0.5)
    print("%.2f" %result)

def enginecheck(engine):
    """enginecheck"""
    price = 0
    if engine > 1800:
        price += (engine-1800)*4
        engine = 1800
    if engine > 600:
        price += (engine-600)*1.5
        engine = 600
    price += engine*0.5
    return price

tax(int(input()), int(input()))
