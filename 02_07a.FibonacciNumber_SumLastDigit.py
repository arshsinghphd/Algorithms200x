dict_fibLastDigit = {0:0, 1:1}
dict_fibSumLastDigit = {0:0, 1:1}

def fibLastDigit(n):
    n = n% 60
    if n <= 1:
        return n
    elif n in dict_fibLastDigit.keys():
        return dict_fibLastDigit[n]
    else:
        dict_fibLastDigit[n] = (fibLastDigit(n-1) + fibLastDigit(n-2)) % 10
        return dict_fibLastDigit[n]

def fibSumLastDigit(n):
    n = n % 60
    if n <= 1:
        return n
    elif n in dict_fibSumLastDigit.keys():
        return dict_fibSumLastDigit[n]
    else: 
        dict_fibSumLastDigit[n] = (fibSumLastDigit(n-1) + fibLastDigit(n)) % 10
        return dict_fibSumLastDigit[n]
    
def brute_force(n):
    if n <= 1:
        return n
    
    prev, curr, sum_= 0, 1, 1
    for _ in range(n - 1):
        prev, curr = curr, (prev + curr) % 10
        sum_ = (sum_ + curr) % 10
    return sum_ % 10

if __name__ == '__main__':
    n = int(input())
    r = fibSumLastDigit(n)
    #b = brute_force(n)
    print('Recursive =', r)
    #print('Brute Force =', b)
    #print(r == b)
