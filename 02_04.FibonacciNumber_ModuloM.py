import time

def fib_cyclicity(m):
    prev = 0
    curr = 1
    counter = 0
    while True:
        counter += 1
        prev, curr = curr, prev + curr
        if prev % m == 0 and curr % m == 1:
            return counter

def fib_number_modulo(n,m):
    c = fib_cyclicity(m)
    n = n % c
    
    if n <= 1:
        return n

    prev = 0
    curr = 1
    for _ in range(n - 1):
        prev, curr = curr, prev + curr

    return curr % m 

if __name__=='__main__':
    n, m = map(int, input().split())
    print(fib_number_modulo(n, m))
