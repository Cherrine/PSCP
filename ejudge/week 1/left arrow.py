"""_"""
def main():
    """_"""
    width = int(input())
    height = int(input())
    count = height // 2
    blank = 1
    if height == 1:
        print(width * "*")
    else:
        while True:
            if height < 0:
                break
            print(height // 2  * " ", end="")
            print(width * "*")
            height -= 2
        while True:
            print(blank * " ", end="")
            print(width * "*")
            blank = blank + 1
            if blank - 1 == count:
                break
main()
