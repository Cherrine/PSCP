def main(firstgrid, secgrid):
    """multiplymatrixpqr"""
    sol = []
    for i in range(0, len(firstgrid), 2):
        num = firstgrid[i:i+2]
        for j in range(0, len(secgrid), 2):
            secnum = secgrid[j:j+2]
            prod = sum([a*b for a,b in zip(num, secnum)])
            sol.append(prod)
    return sol

def gridmaker():
    """multiplymatrixpqr"""
    pgrid = int(input())
    qgrid = int(input())
    rgrid = int(input())

    firstgrid = []
    secgrid = []
    for _ in range(pgrid*qgrid):
        firstgrid.append(int(input()))
    for _ in range(qgrid*rgrid):
        secgrid.append(int(input()))
    return firstgrid, secgrid

firstgrid, secgrid = gridmaker()
result = main(firstgrid, secgrid)
print(result)
