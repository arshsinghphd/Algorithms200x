## Range Sum Queries

## Given an integer array and
## a set of ranges in it compute the sum for each range.

## Input: An integer array (a[0],…,a[n−1])(a[0]​,…,a[n−1]​)
## and q ranges (b[0],e[0]), ..., (b[q−1],e[q−1]).

## Output: For each range (b,e), sum =​ a[b] + ... + a[e - 1]

dict_sumN = {}

def rangeSum(arr): # O(n)
    len_arr = len(arr)
    dict_sumN[0]=arr[0]
    for i in range(1, len_arr):
        dict_sumN[i]=dict_sumN[i-1] + arr[i]
    
if __name__ =='__main__': 
    # read the test case
    f = open('02_10.test.txt', 'r')
    arr = list(map(int, f.readline().strip().split()))
    q = int(f.readline().strip())
    ranges=[]
    for j in range(q):
        ranges.append(list(map(int, f.readline().strip().split())))
        
    # Make the dictionary with all the sums arr[0,0] to arr[0, len_arr - 1]    
    rangeSum(arr)
    
    # make a list of answers
    rangeSums = []
    for r in ranges: # complexity O(q)
        b = r[0]
        e = r[1]
        rangeSums.append(dict_sumN[e] - dict_sumN[b-1])
    print(rangeSums == [8, 4])
