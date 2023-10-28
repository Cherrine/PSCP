"""wpm"""
def wordspermin(ppltype, wpm):
    """type check"""
    if ppltype == "Kids":
        result = kidswpm(wpm)
    elif ppltype == "Adults":
        result = adultswpm(wpm)
    print(result)

def kidswpm(wpm):
    """checks if the type is kids"""
    if wpm < 11:
        return "Very Slow"
    elif wpm > 10 and wpm < 21:
        return "Slow"
    elif wpm > 20 and wpm < 31:
        return "Average"
    elif wpm > 30 and wpm < 41:
        return "Fast"
    elif wpm > 40:
        return "Very Fast"

def adultswpm(wpm):
    """checks if the type is adult"""
    if wpm < 26:
        return "Very Slow"
    elif wpm > 25 and wpm < 36:
        return "Slow/Beginner"
    elif wpm > 35 and wpm < 46:
        return "Intermediate/Average"
    elif wpm > 45 and wpm < 66:
        return "Fast/Advanced"
    elif wpm > 65 and wpm < 81:
        return "Very Fast"
    else:
        return "Insane"

wordspermin(input(), int(input()))
