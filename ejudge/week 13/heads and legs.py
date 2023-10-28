"""heads and legs"""
def headsandlegs(total, legs):
    """function"""
    rabbits = (legs - 2 * total)//2
    birds = total - rabbits
    if rabbits < 0 or birds < 0 or 4 * rabbits + 2 * birds != legs:
        print("Impossible")
    else:
        print(str(rabbits) + " " + str(birds))
headsandlegs(int(input()), int(input()))
