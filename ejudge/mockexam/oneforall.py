"""one for all"""

def hero(sequence, length=""):
    """function"""
    for i in range(1, sequence + 1):
        name = input()
        if i == sequence:
            length += name + "_" + str(i)
        elif i % 2:
            length += name + "*" * i
        else:
            length += name + "-" * i
    print(length)
hero(int(input()))
