"""Docstring"""
def main():
    """Bonus"""
    salary = int(input())
    years = int(input())
    months = int(input())
    bonus = 0
    mutiply = 0
    if months >= 10:
        mutiply += 1
    else:
        mutiply += 0
    if years > 0 and years <= 20:
        mutiply += years
    elif years > 20:
        mutiply += 20
    elif years == 0:
        mutiply += 0
    bonus = salary * mutiply
    if bonus > 20 * salary:
        bonus = 20 * salary
    if bonus <= 1000000 and bonus > 5000:
        print(bonus)
    elif bonus <= 5000:
        print(5000)
    elif bonus > 1000000:
        print(1000000)
main()
