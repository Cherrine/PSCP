"""prasomsib"""
def prasomsib(numset):
    paircount = 0
    numsetstr = str(numset)
    num = 0
    while num < (len(numsetstr)-1):
        if int(numsetstr[num]) + int(numsetstr[num+1]) == 10:
            paircount += 1
            num += 2
        else:
            num += 1
    print(paircount)
prasomsib(int(input()))