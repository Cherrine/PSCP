a = int(input())
for x in range(a):
    for y in range(a - x - 1):
        print(" ", end="  ")
    for y in range(x + 1):
        print(y+1, end="|")
    for y in range(x, 0, -1):
        print(y, end="|")
    print()
