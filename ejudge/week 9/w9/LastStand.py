"""doc"""
import json
def main():
    """string"""
    number = input()
    listednum = json.loads(number)
    for num in listednum:
        rnum = str(num)
        lastdigitstr = rnum[-1]
        lastdigit = int(lastdigitstr)
        print(lastdigit)
main()
