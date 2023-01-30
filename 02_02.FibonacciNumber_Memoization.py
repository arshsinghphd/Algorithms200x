# Time Limit 5 secs
# Memory Limit 512 MB
# Max n=45
import time
start=time.perf_counter()

fibonacci={}

def fibonacci_number(n):
    if n <= 1:
        fibonacci[n]=n
    else:
        if n not in fibonacci.keys():
            fibonacci[n]=fibonacci_number(n-1)+fibonacci_number(n-2)
            
    return fibonacci[n]

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))


end=time.perf_counter()
print(f"{end - start}")
