""" Two Solutions provided - Iterative and Recurance
    Both have O(n) time complexity, however Recursive method has
    O(n) spave complexity
    No check for -ve number done
"""

def FactRecur(num):
    if num == 0:
        return 1
    return num*FactRecur(num-1)

def FactIter(num):
    res = 1
    if num == 1:
        return res

    for i in range(2, num+1):
        res *= i

    return res

if __name__ == '__main__':
    print(FactIter(5))
    print(FactRecur(5))