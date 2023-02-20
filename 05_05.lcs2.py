def lcss(list1, list2, n, m):
    '''
    given: two list of integers.
    return: the length of the longest common subsequence between them.
    note: there may be many subsequences
    '''
    D = [[0 for j in range(m + 1)] for i in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                D[i][j] = 0
            else:
                D[i][j] = max(D[i - 1][j],
                              D[i][j - 1],
                              D[i - 1][j - 1]\
                              + 1*(list1[i - 1] == list2[j - 1])
                )
        
    return D[n][m]

if __name__ == '__main__':
    print(lcss([2, 7, 3, 8, 5],  [2, 3, 8, 7], 5, 4))
    print(lcss([7],  [1, 2, 3, 4], 1, 4))
    print(lcss([2, 7, 5], [2, 5], 3, 2))
    
#    print(lcss(int(input().split()), int(input().split())))
