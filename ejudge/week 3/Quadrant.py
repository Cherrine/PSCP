"""_"""
def main():
    """_"""
    xnum1 = int(input())
    ynum2 = int(input())
    if xnum1 == 0 and ynum2 == 0:
        print("O")
    elif xnum1 == 0:
        print("Y")
    elif ynum2 == 0:
        print("X")
    elif xnum1 > 0 and ynum2 > 0:
        print("Q1")
    elif xnum1 < 0 and ynum2 > 0:
        print("Q2")
    elif xnum1 < 0 and ynum2 < 0:
        print("Q3")
    elif xnum1 > 0 and ynum2 < 0:
        print("Q4")
main()
