"""calculator v2"""
def main(cal, tmp):
    """function"""
    if cal <= 9:
        if cal <= 1:
            return 1
        return cal*2
    callen = len(str(cal))
    for i in range(callen-1):
        tmp += int("9"+"0"*i) * (i+2)
    tmp += (cal-int("9"*(callen-1))) * (callen+1)
    return tmp
print(main(int(input()), 0))
