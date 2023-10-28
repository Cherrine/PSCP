"""duplicate i"""
def dupe():
    """function"""
    numgroup1 = int(input())
    numgroup2 = int(input())
    group1 = set()
    group2 = set()
    for _ in range(numgroup1):
        group1.add(int(input()))
    for _ in range(numgroup2):
        group2.add(int(input()))
    for i in sorted(group1.intersection(group2), reverse=True):
        print(i)
    if not group1.intersection(group2):
        print("Nope")
dupe()
