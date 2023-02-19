import numpy as np

def editDistance(s_1, s_2):
    n = len(s_1)    
    m = len(s_2)

##  create empty matrix 
    D = np.array([[0 for i in range(m + 1)] for j in range(n + 1)])

    D[0][0] = 0
    for j in range(1, m + 1):
        D[0][j] = j
        
    for i in range(1, n + 1):
        D[i][0] = i
        
##  fill the matrix
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            Ins = D[i][j - 1] + 1
            Del = D[i - 1][j] + 1
            Mat = D[i - 1][j - 1]
            Mis = D[i - 1][j - 1] + 1
            if s_1[i-1] == s_2[j-1]:
                D[i][j] = min(Ins, Del, Mat)
            else:
                D[i][j] = min(Ins, Del, Mis)

    for i in D:
        print(i)
        
    return D[n][m]

if __name__=='__main__':
    
    print(editDistance('editing', 'distance'))
