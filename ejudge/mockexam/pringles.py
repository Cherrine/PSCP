"""pringles"""

def prongo(box_top, lay, box_bot, finger, total=0):
    """function"""
    for i in lay[:finger]:
        if i == ")":
            total += 1
    print(total)
    total = 0
    for i in lay[finger:]:
        if i == ")":
            total += 1
    if total == 0:
        print("None.")
    else:
        print("There are still some left.")
    print(box_top + "\n" + " " * finger + "%s\n%s" %(lay[finger:], box_bot))
prongo(input(), input(), input(), int(input()))
