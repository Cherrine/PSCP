"""key"""
def key():
    """function"""
    num = input()
    numbers = num[-3:]
    total = 0
    for digit in num:
        total += int(digit)
    lastthree = int(numbers) * 10
    summary = total + lastthree
    if summary >= 10000:
        print(str(summary)[-4:])
    elif summary < 1000:
        summary += 1000
        print(summary)
    else:
        print(summary)
key()
