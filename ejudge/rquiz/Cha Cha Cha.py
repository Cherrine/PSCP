"""Cha Cha Cha"""
def salary(days, total=0):
    """calculate"""
    for _ in range(days):
        hours = float(input())
        if hours % 1 != 0:
            hours = hours // 1 + 1
        total += 8720* hours
    print(int(total))
salary(int(input()))
