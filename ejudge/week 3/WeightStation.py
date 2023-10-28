"""_"""
def main(average, weight1, weight2, weight3):
    """_"""
    totalweight = weight1 + weight2 + weight3
    result = ""
    if totalweight > 15000:
        result = "Overweight"
    else:
        maxhalfweight = average / 2
        missingweight = (average * 4) - (totalweight)
    
        if abs(average - weight1) > maxhalfweight or \
            abs(average - weight2) > maxhalfweight or \
            abs(average - weight3) > maxhalfweight:
            result = "Unbalanced"
        else:
            result = "Pass"
    return result, missingweight

average = int(input())
weight1 = int(input())
weight2 = int(input())
weight3 = int(input())

result, missingweight = main(average, weight1, weight2, weight3)
if result == "Unbalanced":
    print("Unbalanced")
elif result == "Overweight":
    print("Overweight")
else:
    roundmissingweight = "%.2f" %missingweight
    print(result, roundmissingweight)