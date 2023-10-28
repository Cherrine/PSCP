"""RockPaperScissor"""


def score_result(p1_score, p2_score):
    """Define the winner"""
    if p1_score > p2_score:
        print("A win {0}-{1}".format(p1_score, p2_score))
    elif p2_score > p1_score:
        print("B win {1}-{0}".format(p1_score, p2_score))
    else:
        print("DRAW {}".format(p1_score))


def rps_game(text):
    """Calculate who's winning"""
    p1_score = 0
    p2_score = 0
    for i in range(0, len(text), 2):
        p_1 = text[i]
        p_2 = text[i + 1]
        if p_1 == "R":
            if p_2 == "P":
                p2_score += 1
            elif p_2 == "S":
                p1_score += 1
        elif p_1 == "P":
            if p_2 == "S":
                p2_score += 1
            elif p_2 == "R":
                p1_score += 1
        elif p_1 == "S":
            if p_2 == "R":
                p2_score += 1
            elif p_2 == "P":
                p1_score += 1
    score_result(p1_score, p2_score)


rps_game(str(input()))
