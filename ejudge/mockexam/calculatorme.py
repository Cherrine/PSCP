"""calculator"""

def calc(typing, num=""):
    """function"""
    for i in range(1, typing + 1):
        num += str(i) + "+"
    if typing == 1:
        return print(1)
    print(len(num))
calc(int(input()))
