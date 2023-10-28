"""lift"""
def main(ppl, fullweight):
    adult = 0
    currweight = 0
    for _ in range(ppl):
        age = 0
        weight = 0
        age = int(input())
        if age < 12:
            pass
        else:
            adult += 1
        weight = float(input())
        if age >= 12 and weight <= 0:
            adult -= 1
        else:
            currweight += weight
    if adult <= 0 or fullweight < currweight:
        print("Not Safe")
    
    else:
        print("Safe")

main(int(input()), float(input()))