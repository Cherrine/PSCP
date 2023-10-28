"""backward"""
def backward():
    """calculate"""
    word = []
    while True:
        text = str(input())
        if text == "NULL":
            break
        word.append(text)
    reversedword = list(reversed(word))
    for word in reversedword:
        print(word)
backward()
