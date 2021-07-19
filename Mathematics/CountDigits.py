def CountDigits(num):
    sum = 0
    while num > 0:
        num = int(num/10)
        sum += 1
    return sum

if __name__ == '__main__':
    num = 129758758575865865865
    print(CountDigits(num)) 