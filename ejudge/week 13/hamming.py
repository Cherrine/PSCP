"""hamming"""
def hamming(word1, word2):
    """function"""
    print(sum(char1 != char2 for char1, char2 in zip(word1, word2)))
hamming(input(), input())
