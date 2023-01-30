import sys

def gcd(a,b):
    if b == 0:
        return a
    a2 = a%b
    return gcd(b, a2)

def lcm(a, b):
    gcd_ab = gcd(a, b)
    return (b * a) // gcd_ab
    
if __name__=='__main__':
    #a, b = map(int, input().split())
    a=226553150
    b=1023473145
    
    print(lcm(a, b))
