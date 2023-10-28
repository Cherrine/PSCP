"""flatten"""

import json

def flat(value: list):
    """function"""
    lis = []
    for i in value:
        if isinstance(i, list):
            lis += flat(i)
        else:
            lis.append(i)
    lis.sort(reverse=True)
    return lis

print(flat(json.loads(input())))
