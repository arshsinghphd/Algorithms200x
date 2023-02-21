def fillSack(cap, bars):
    '''
    Filling True/1 or False/0 in cells
    If a cell represent a weight that can be achieved
    using the bars, it is filled with 1 (True)
    else, it is filled with false.
    '''
    n = len(bars)
    D = [[False for i in range(n + 1)] for w in range(cap + 1)]
    D[0][0] = True
    for w in range(cap + 1):
        for i in range(1, n + 1):
            #if cap (w) is full, skip rest of the bars
            if D[w][i - 1] > w: 
                D[w][i] = D[w][i - 1]
            else:
                D[w][i] = D[w][i - 1] or D[w - bars[i - 1]][i - 1]
                
    return D[w][n]

print(fillSack(8, [4,3,1]))
    
