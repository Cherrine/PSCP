"""PickThem"""
import json
def main():
    """cal"""
    number = input()
    listednum = json.loads(number)
    snum = [num for num in listednum if num%2 == 0]
    if snum:
        for num in snum:
            print(num)
    else:
        print("Nope")
main()
