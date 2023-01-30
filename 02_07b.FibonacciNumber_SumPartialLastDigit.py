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

def fibPartialSumLastDigit(from_, to):
    sum_to = fibSumLastDigit(to)
    sum_from = fibSumLastDigit(from_ - 1)
    reqd_sum = (sum_to - sum_from) % 10
    if reqd_sum >= 0:
        return reqd_sum
    else:
        return 10 + reqd_sum
    
if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibPartialSumLastDigit(from_, to))
