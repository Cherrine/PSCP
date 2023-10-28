"""thefunctionwithin"""
def calculate(vala, valb, valc, vald):
    print(funcf(funcf(vala)))
    print(funcg(funcf(vala-valb)))
    print(funch(funcf(vala+valb)), funcf(vala+valc), funcg(funcf(vald**2)))
    print(funci(funch(funcf(vala+valb))), funcf(vala-valc), funcg(funcf(vald**2)),\
        funcg(funcf(vala-valb)), funcf(funcf(funcf(funcf(funcf(valc))))), vald**8)
def funcf(valx):
    """f(x)"""
    return valx*2

def funcg(valx):
    """g(x)"""
    return 3*valx**4 - valx**3 + 2*valx**2 + 10

def funch(valx, valy, valz):
    """h(x)"""
    return (valz+valx)**2 - valx*valy + valy**2

def funci(vala, valb, valc, vald):
    """i(x)"""
    return (vala**2 + valb**2 - valc**2) / (vald**2 - 2*vala*vald + 2**vala)

calculate()
