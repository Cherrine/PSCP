""" GraderMachine """
def main(ton, fob):
    """ GraderMachine """
    total = 0
    print("pass :", end=" ")
    if ton > fob:
        for i in range(ton, (fob - 1), -1):
            if i % 2 == 0:
                total += i
                print("%d" % i, end=" ")
    elif ton <= fob:
        for i in range(ton, fob + 1):
            if i % 2 == 0:
                total += i
                print("%d" % i, end=" ")
    print()
    print("Sum : %d" % total)
main(int(input()), int(input()))