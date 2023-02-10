
def max_dot_product(profits, clicks):
    '''
    Given:
    list profits: a_0, ..., a_n and
    list clicks: number of clicks per day b_0, ..., b_n

    Return:
    max possible dot product of the lists.
    '''
    profits.sort()
    clicks.sort()
    
    for i in range(len(clicks)):
        result += profits[i] * clicks[i]

    return result

if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
    
