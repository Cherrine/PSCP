"""Easy Histogram"""
def histogram():
    """function"""
    text = input()
    chars = []
    totals = []

    for char in text:
        if char.isalpha():
            if char in chars:
                index = chars.index(char)
                totals[index] += 1
            else:
                chars.append(char)
                totals.append(1)

    def sort_key(pair):
        """FUNCTION"""
        char, _ = pair
        return char.lower(), char.isupper(), char

    sorted_chars = sorted(zip(chars, totals), key=sort_key)

    for i in range(len(sorted_chars)):
        char, total = sorted_chars[i]
        print(char + ' = ' + str(total))

histogram()
