## O(min(a, b)) complexity 
def GCDNaive(a, b):
    res = min(a, b)
    while res > 0:
        if a%res == 0 and b%res == 0:
            return res
        res -= 1

## Euclid 
def GCDEuclid(a, b):
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a

def GCDOptmized(a, b):
    if (b == 0):
        return a
    else:
        return GCDOptmized(b, a%b)

if __name__ == '__main__':
    print(GCDOptmized(1024, 512*3))