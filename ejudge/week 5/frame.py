"""frame"""
def frame(txt):
    """function"""
    print(len(txt)*"*", "**", sep="")
    print("*", txt, "*", sep="")
    print(len(txt)*"*", "**", sep="")
frame(input())
