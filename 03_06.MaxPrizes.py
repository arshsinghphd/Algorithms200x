def maxPrizes(n):
    '''
    Represent a positive integer as the sum of the maximum number of pairwise
    distinct positive integers.
    Input: A positive integer n.
    Output: The maximum k such that n can be represented as the sum
    a_1 + ... + a_k of k distinct positive integers
    '''
#   guess the closest k as guess, g = int(sqrt(2n) - 1)
#   keep trying next g with reducing steps of sqrt(n - g*(g + 1)/2)
    g = int((2*n)**(1/2) - 1)
    while int(n - (g * (g + 1) / 2)) >= 0:
        prev_g = g
        #step = int((n - (g*(g + 1)/2))**.5)
        step = 1
        g = prev_g + step

    return prev_g

if __name__=='__main__':
    n=int(input())
    k=maxPrizes(n)
    dist=list(range(1,k+1))
    diff = n - int(k*(k+1)/2)
    for i in range(k-diff,k):
        dist[i] += 1
    print(k)
    print(*dist)                
