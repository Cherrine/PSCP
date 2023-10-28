"""hamburger"""
def hamb(lbun, rbun):
    """cal"""
    print("|"*lbun, "*"*((lbun+rbun)*2), "|"*rbun, sep="")
hamb(int(input()), int(input()))
