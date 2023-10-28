"""Virus I"""
def virusi(body):
    """count"""
    count = 0
    for i in body:
        if i.islower():
            count += 1
    print(count)
virusi(input())
