import numpy as np

def editDistance(s1, s2):
    n = len(s1)
    m = len(s2)
    D = np.array([[0 for x in range(m + 1)] for x in range(n + 1)])
    
    for j in range(1, m + 1):
        D[0][j] = j 
        
    for i in range(1, n + 1):
        D[i][0] = i
    
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            Ins = D[i][j - 1] + 1
            Del = D[i - 1][j] + 1
            Mat = D[i - 1][j - 1]
            Mis = D[i - 1][j - 1] + 1
            if s1[i - 1] == s2[j - 1]:
                D[i][j] = min(Ins, Del, Mat)
            else:
                D[i][j] = min(Ins, Del, Mis)
                
    return D

def editSequence(s1, s2):
    D = editDistance(s1, s2)
    s1 = [i for i in s1]
    s2 = [j for j in s2]
    print(D)
    s1_opt = ''
    s2_opt = ''
    i, j = len(D) - 1, len(D[0]) - 1
    
    while i > 0 or j > 0:
        if D[i][j] == D[i - 1][j] + 1 and i > 0 :
            # inserted
            s1_opt = s1[i - 1] + '|' + s1_opt
            s2_opt = '-|' + s2_opt
            i -= 1
        elif D[i][j] == D[i][j - 1] + 1 and j > 0 :
            # deleted
            s1_opt = '-|' + s1_opt
            s2_opt = s2[j - 1] + '|' + s2_opt
            j -= 1
        else:
            # match or mismatch
            s1_opt = s1[i - 1] + '|' + s1_opt
            s2_opt = s2[j - 1] + '|' + s2_opt
            i -= 1
            j -= 1

    return '|' + s1_opt + '\n' + '|' + s2_opt
    
print(editSequence('editing','distance'))
