def largest_number(num1, num2, num3):
    con1 = num1 > num2 > num3
    con2 = num1 > num3 > num2
    con3 = num2 > num1 > num3
    con4 = num2 > num3 > num1
    con5 = num3 > num2 > num1
    con6 = num3 > num1 > num2
    
    if con1:
        return num1 * 100 + num2 * 10 + num3
    elif con2:
        return num1 * 100 + num3 * 10 + num2
    elif con3:
        return num2 * 100 + num1 * 10 + num3
    elif con4:
        return num2 * 100 + num3 * 10 + num1
    elif con5:
        return num3 * 100 + num2 * 10 + num1
    elif con6:
        return num3 * 100 + num1 * 10 + num2

num1 = int(input())
num2 = int(input())
num3 = int(input())

result = largest_number(num1, num2, num3)
print(result)
