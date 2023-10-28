"""_"""
def main(total, highest):
    """_"""
    lowest = total - (highest * 2)
    if highest - lowest > 2:
        print("Surprising")
    else:
        print("Not Surprising")
main(float(input()), float(input()))
