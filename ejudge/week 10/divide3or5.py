"""divide 3 or 5"""
def sum_numbers(base):
    """function"""
    base = int(base)
    total = 0
    for i in range(1, base+1):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total
print(sum_numbers(float(input())))
