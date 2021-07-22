## Time Complexity log(min(a,b))
def GCD(a, b):
    if (b == 0):
        return a
    else:
        return GCD(b, a%b)

def LCM(a, b):
    return int(a*b/GCD(a, b))

if __name__ == '__main__':
    print(LCM(17, 21))