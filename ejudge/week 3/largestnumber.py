"""largestnumber"""
def main(aaa, bbb, ccc):
    """main"""
    condi1 = int(aaa+bbb+ccc)
    condi2 = int(aaa+ccc+bbb)
    condi3 = int(bbb+aaa+ccc)
    condi4 = int(bbb+ccc+aaa)
    condi5 = int(ccc+aaa+bbb)
    condi6 = int(ccc+bbb+aaa)

    largest = condi1
    if condi2 > largest:
        largest = condi2
    if condi3 > largest:
        largest = condi3
    if condi4 > largest:
        largest = condi4
    if condi5 > largest:
        largest = condi5
    if condi6 > largest:
        largest = condi6

    print(largest)

main(input(), input(), input())
