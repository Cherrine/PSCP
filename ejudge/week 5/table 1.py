"""table 1"""
def table():
    """function"""
    count = int(input())
    for times in range(count):
        res = 15 * (times+1)
        print("15 x", times+1, "=", res)
table()
