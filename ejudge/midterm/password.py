"""Password"""
def main():
    """function"""
    import math
    txt = input()
    num = 0
    lowkey = 0
    highkey = 0
    special = 0
    count = 0
    for i in txt:
        if i.islower():
            lowkey = 26
        elif i.isupper():
            highkey = 26
        elif i.isnumeric():
            num = 10
        elif i.isprintable():
            special = 32
        count += 1
    rrr = lowkey + highkey + special + num
    result = math.log2(rrr ** count)
    print(int(result))
    result = int(result)
    if result < 28:
        print("Very Weak")
    elif result <= 35:
        print("Weak")
    elif result <= 59:
        print("Reasonable")
    elif result <= 127:
        print("Strong")
    else:
        print("Very Strong")
main()
