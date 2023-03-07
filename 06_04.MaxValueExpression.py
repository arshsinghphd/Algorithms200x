import re

def evaluate(n, m, op):
    n = int(n)
    m = int(m)
    if op == '+':
        return n + m
    elif op == '-':
        return n - m
    else:
        return n * m 
    
def minAndMax(ops, i, j, m, M):
    m_ = 10**9
    M_ = -1*10**9
    for k in range(i, j):
        a = evaluate(M[i][k], M[k + 1][j], ops[k])
        b = evaluate(M[i][k], m[k + 1][j], ops[k])
        c = evaluate(m[i][k], M[k + 1][j], ops[k])
        d = evaluate(m[i][k], m[k + 1][j], ops[k])
        m_ = min(m_, a, b, c, d)
        M_ = max(M_, a, b, c, d)
    return m_, M_
    
def addParenthesis(s):
    ops = []
    nums = []
    for ch in re.split('(\D)', s) :
        if ch in ['-','+','*']:
            ops.append(ch)
        else:
            nums.append(int(ch))

    n = len(nums)
    M = [[0 for i in nums] for j in nums]
    m = [[0 for i in nums] for j in nums]

    # fill diagonals
    for i in range(n): 
        M[i][i] = nums[i]
        m[i][i] = nums[i]

    # fill rest of the tables m and M
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            m[i][j], M[i][j] = minAndMax(ops, i, j, m, M)

    return M[0][n - 1]
            
if __name__ == '__main__':
##    print(addParenthesis(input()))
    print(addParenthesis('5-8+7*4-8+9')==200)
