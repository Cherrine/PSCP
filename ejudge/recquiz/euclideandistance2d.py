"""euclideandistance2d"""
def calculate(pointq1, pointq2, pointp1, pointp2):
    """cal"""
    print(((pointq1 - pointp1)**2 + (pointq2 - pointp2)**2)**0.5)
calculate(float(input()), float(input()), float(input()), float(input()))
