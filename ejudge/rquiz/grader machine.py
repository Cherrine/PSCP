"""_"""
def main():
    """_"""
    start_weight = int(input())
    end_weight = int(input())

    selected_weights = ""
    total_weight = 0

    weight = start_weight
    if start_weight > end_weight:
        for i in range(start_weight, (end_weight - 1), -1):
            if i % 2 == 0:
                selected_weights += str(i) + " "
                total_weight += i
    while weight <= end_weight:
        if weight % 2 == 0:
            selected_weights += str(weight) + " "
            total_weight += weight
        weight += 1

    print("pass :", selected_weights.rstrip())
    print("Sum :", total_weight)

main()
