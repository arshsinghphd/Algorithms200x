dict_fibLastDigit = {0:0, 1:1}
dict_fibSqSumLastDigit = {0:0, 1:1}

def fibLastDigit(n):
    n = n%60
    if n <= 1:
        return n
    elif n in dict_fibLastDigit.keys():
        return dict_fibLastDigit[n]
    else:
        dict_fibLastDigit[n] = (fibLastDigit(n-1) + fibLastDigit(n-2)) % 10
        return dict_fibLastDigit[n]

def fibSqSumLastDigit(n):
    n = n % 60
    if n <= 1:
        return n
    elif n in dict_fibSqSumLastDigit.keys():
        return dict_fibSqSumLastDigit[n]
    else: 
        dict_fibSqSumLastDigit[n] = (fibSqSumLastDigit(n-1) + fibLastDigit(n)**2) % 10
        return dict_fibSqSumLastDigit[n]

if __name__ == '__main__':
    n = int(input())
    r = fibSqSumLastDigit(n)
    print(r)
