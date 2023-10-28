"""_"""
def check_weight_balance():
    """_"""
    average = float(input())
    weight1 = float(input())
    weight2 = float(input())
    weight3 = float(input())
    totalweight = weight1 + weight2 + weight3
    result = ""
    overweight = False
    unbalanced = False
    if totalweight >= 15001:
        overweight = True
    else:
        maxhalfweight = average / 2
        missingweight = (average * 4) - (totalweight)

        if totalweight + missingweight >= 15001:
            overweight = True

        elif abs(average - weight1) > maxhalfweight or \
            abs(average - weight2) > maxhalfweight or \
            abs(average - weight3) > maxhalfweight or \
            abs(average - missingweight) > maxhalfweight:
            unbalanced = True

        else:
            result = "Pass"

    if result == "Pass":
        print("Pass", "%.2f" %missingweight)
    elif overweight is True and unbalanced is True:
        print("Overweight")
    elif overweight is True:
        print("Overweight")
    elif unbalanced is True:
        print("Unbalance")

check_weight_balance()
