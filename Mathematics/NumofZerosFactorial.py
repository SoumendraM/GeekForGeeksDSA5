""" The number of zeros can be defines as the number of multiples of 5, 25, 125...... in the factors
"""
def NumOfZerosFactorial(num):
    res = 0
    i = 5
    while i <= num:
        res += int(num/i)
        print
        i = i*5
    return res

if __name__ == '__main__':
    print(NumOfZerosFactorial(251)) 