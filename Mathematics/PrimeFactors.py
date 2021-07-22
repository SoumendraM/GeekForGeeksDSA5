def PrimeFactors(num):
    if num == 1:
        return 1
    
    i = 2
    while i*i <= num:
        while num%i == 0:
            print(i, end = ' ')
            num = int(num/i)
        i += 1
    if num > 1:
        print(num)

def PrimeFactorsEff(num):
    if num == 1:
        return 1
    
    for i in (2, 3):
        while num % i == 0:
            print(i, end=' ')
            num = int(num/i)
        
    i = 5
    while i*i <= num:
        while num%i == 0:
            print(i, end = ' ')
            num = int(num/i)
            
        while num%(i+2) == 0:
            print(i+2, end = ' ')
            num = int(num/(i+2))
        i += 6
    if num > 1:
        print(num)    

if __name__ == '__main__':
    PrimeFactorsEff(1749150)