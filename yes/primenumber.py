def main(num):
    flag = False
    if num == 1:
        print("no prime number")
    for i in range(2, num):
        if num % i == 0:
            flag = True
            break
    if flag:
        print("no prime number")
    else:
        print("prime number")
main(int(input()))