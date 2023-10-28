"""gacha"""
def lotto_number():
    main_num = int(input())
    last2_num = int(input())
    frfront3_num = int(input())
    sefront3_num = int(input())
    frlast3_num = int(input())
    selast3_num = int(input())
    nearmain_num = int(input())
    return main_num, last2_num, frfront3_num, sefront3_num, frlast3_num, selast3_num, nearmain_num


def lotto(main_num, last2_num, frfront3_num, sefront3_num, frlast3_num, selast3_num, nearmain_num):
    your_lotto = int(input())
    prize = 0
    if main_num in your_lotto:
        prize += 6000000
    if last2_num in your_lotto:
        prize += 2000
    if front3_num or last3_num in your_lotto:
        prize += 4000
    if 
            