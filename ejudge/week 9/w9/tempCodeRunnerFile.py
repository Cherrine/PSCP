"""tuplesadlife"""
import json
def main():
    """function"""
    number = input()
    count = int(input())
    text = json.loads(number)
    index = text.index(count)
    print(index)
main()
    