"""Difference"""

def diff(nnum, mnum):
    """Function"""
    set_a = set()
    for _ in range(nnum):
        set_a.add(int(input()))
    for _ in range(mnum):
        set_a.discard(int(input()))
    for i in sorted(set_a):
        print(i, end=" ")
diff(int(input()), int(input()))
