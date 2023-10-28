"""pointsorting"""
def main():
    """function"""
    num = int(input())
    listpoint = []
    for _ in range(num):
        numlist = int(input())
        for _ in range(numlist):
            listpoint.append(tuple(map(int, input().split())))
        listpoint.sort(reverse=True, key=lambda x: x[1])
        listpoint.sort(key=lambda x: x[0]+x[1])
        for i in range(numlist):
            print(listpoint[i][0], listpoint[i][1])
        listpoint = []
main()
