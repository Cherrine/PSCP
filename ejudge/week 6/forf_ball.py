"""FOR!F-Ball"""


def swapper(seq, a_cup, b_cup, c_cup):
    """Swapping sequence"""
    if seq == "A":
        a_cup, b_cup = b_cup, a_cup
    elif seq == "B":
        b_cup, c_cup = c_cup, b_cup
    else:
        a_cup, c_cup = c_cup, a_cup
    return a_cup, b_cup, c_cup


def main():
    """Main func"""
    a_cup, b_cup, c_cup = 1, 0, 0
    text = str(input())
    for seq in text:
        a_cup, b_cup, c_cup = swapper(seq, a_cup, b_cup, c_cup)
    result = "{}{}{}".format(a_cup, b_cup, c_cup)
    print(result.index("1") + 1)


main()
