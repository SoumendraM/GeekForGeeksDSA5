def Palin(num):
    tmp = num
    rev = 0
    while tmp > 0:
        dig = tmp%10
        rev = rev*10 + dig
        tmp = int(tmp/10)
    if rev == num:
        return True
    else:
        return False

if __name__ == '__main__':
    num = 12345678987654321
    print(Palin(num))