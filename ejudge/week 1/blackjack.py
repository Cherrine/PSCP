"""_"""
def main():
    """_"""
    case = int(input())
    total = 0
    count = 0
    for _ in range(case):
        card = input()
        if card in ("J", "K", "Q"):
            total = total + 10
        elif card == ("A"):
            total = total + 11
            count = count + 1
        else:
            total = total + int(card)
    for _ in range(count):
        if total > 21:
            total = total - 10
    print(total)
main()
