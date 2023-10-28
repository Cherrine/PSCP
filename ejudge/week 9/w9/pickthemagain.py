"""PickThem"""
def main():
    """cal"""
    number = input()
    listnum = list(map(int, number.split()))
    snum = [num for num in listnum if num%5 == 0 or num%3 == 0]
    if snum:
        for num in reversed(snum):
            print(num)
    else:
        print("Nope")
main()
