import sys

def gcd(a,b):
    if b == 0:
        return a
    a2 = a % b
    return gcd(b, a2)

if __name__=='__main__':
    #input = sys.stdin.read()
    a, b = map(int, input().split())
    print(gcd(a, b))
