"""AscendingSort"""
def main():
    """cal"""
    number = []
    for _ in range(5):
        num = int(input())
        number.append(num)
    number.sort()
    for nums in number:
        print(nums)
main()
