import time

def fib_last_digit(n):
    """
    This code returns the last digit of the nth fibonacci number as an integer
    """
    n = n%60
    if n <= 1:
        return n
    
    prev = 0
    curr = 1
    for _ in range(n - 1):
        prev, curr = curr, prev + curr
    return curr % 10

if __name__ == '__main__':
    n = int(input())
    start = time.perf_counter()
    print(fib_last_digit(n))
    end = time.perf_counter()
    print(end - start)
