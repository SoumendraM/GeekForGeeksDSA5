## Time Complexity is O(sqrt(n))
def Prime(num):
    if num == 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

## Time Complexity is O(sqrt(n)/5)
def PrimeOpt(num):
    if num == 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    i = 5
    while i*i <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    print(Prime(21646621)) ##  479001599 87178291199
    #PrimeOpt(21646621)