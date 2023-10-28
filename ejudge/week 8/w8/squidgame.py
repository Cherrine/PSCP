"""squidgame"""
def main():
    """results"""
    totala = 0
    totalb = 0
    for _ in range(10):
        num1 = int(input())
        totala += num1
    for _ in range(10):
        num2 = int(input())
        totalb += num2
    if totala > totalb:
        print("B")
    elif totalb > totala:
        print("A")
    else:
        print("AB")
main()
