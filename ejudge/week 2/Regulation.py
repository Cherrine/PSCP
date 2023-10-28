"""jfids"""
def main():
    """lfksldf"""
    numx = int(input())
    numy = float(input())
    numz = input()
    text1 = str(numx).rjust(30)
    if numx < 0:
        text2 = "-" + str(abs(numx)).rjust(29, "0")
    else:
        text2 = str(numx).rjust(30, "0")
    text3 = numz.rjust(40)
    print(text1)
    print(text2)
    print("%.2f" %numy)
    print("%.12f" %numy)
    print(text3)
main()
