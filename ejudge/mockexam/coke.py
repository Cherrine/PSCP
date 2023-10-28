"""coke"""
def main():
    """function"""
    price = int(input())
    change = int(input())
    proprice = int(input())
    want = int(input())
    money = 0
    if change == 0:
        money += want*price
    elif proprice <= price:
        promotion = want//change
        money += promotion*proprice
        if want % change == 0 and want//change != 0:
            promotion -= 1
            money -= proprice
        money += (want-promotion)*price
    print(money)
main()
