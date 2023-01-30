# Time Limit 5 secs
# Memory Limit 512 MB
# Max n=45
import time
start=time.perf_counter()

def fibonacci_number(n):
    if n <= 1:
        return n
    else:
        l_fib = [1,1]
        for e in range(2,n):
            f = l_fib [0] + l_fib[1]
            l_fib.append(f)
            l_fib.pop(0)
        return l_fib[1]
        
if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))

end=time.perf_counter()
print(f"{end - start}")
