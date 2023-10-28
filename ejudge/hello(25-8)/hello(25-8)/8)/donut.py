"""donut"""
def donut(dprice, bonus, free, buy):
    value = bonus + free
    amount = dprice * bonus
    num = buy // value
    remain = buy - (num*value)
    if remain >= amount:
        num += 1
        remain = 0
    print("%d %d" %(num * amount + remain * dprice, num * value + remain))
donut(int(input()), int(input()), int(input()), int(input()))