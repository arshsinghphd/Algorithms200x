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
    
def makeTables(ops, nums):
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

    return m, M

def tracePath(A, i, j, m, M, ops, list_p):
    if i >= 0 and j >= 0:
        for k in range(i, j):
            if A[i][j] == evaluate(M[i][k], M[k + 1][j], ops[k]):
                if i != k:
                    list_p.extend([(i, k)])
                if k + 1 != j:
                    list_p.extend([(k + 1, j)])
                tracePath(M, i, k, m, M, ops, list_p)
                tracePath(m, k + 1, j, m, M, ops, list_p)
            elif A[i][j] == evaluate(M[i][k], m[k + 1][j], ops[k]):
                if i != k:
                    list_p.extend([(i, k)])
                if k + 1 != j:
                    list_p.extend([(k + 1, j)])
                tracePath(M, i, k, m, M, ops, list_p)
                tracePath(m, k + 1, j, m, M, ops, list_p)
            elif A[i][j] == evaluate(m[i][k], M[k + 1][j], ops[k]):
                if i != k:
                    list_p.extend([(i, k)])
                if k + 1 != j:
                    list_p.extend([(k + 1, j)])
                tracePath(m, i, k, m, M, ops, list_p)
                tracePath(M, k + 1, j, m, M, ops, list_p)
            elif A[i][j] == evaluate(m[i][k], m[k + 1][j], ops[k]):
                if i != k:
                    list_p.extend([(i, k)])
                if k + 1 != j:
                    list_p.extend([(k + 1, j)])
                tracePath(m, i, k, m, M, ops, list_p)
                tracePath(m, k + 1, j, m, M, ops, list_p)
    else:
        return

def beautify(s, list_p):
    ans = s
    prev = []
    for b, e in list_p:
        ins = len([i for i in prev if i <= b])
        ans = ans[: 2 * b + ins] + '(' + ans[2 * b + ins:]
        prev.append(b)
        
        ins = len([i for i in prev if i <= e])
        if 2 * e + ins < len(ans) - 1:
            ans = ans[:2 * e + ins + 1] + ')' + ans[2 * e + ins + 1:]    
        else:
            ans = ans + ')'
        prev.append(e)
        print(ans)
    return ans    

def addParenthesis(s):
    ops = []
    nums = []
    for ch in s:
        if ch in ['-','+','*']:
            ops.append(ch)
        else:
            nums.append(int(ch))
    n = len(nums)
    m, M = makeTables(ops, nums)
    list_p = []
    tracePath(M, 0, n - 1, m, M, ops, list_p)
    ans = beautify(s, list_p)
    print(M[0][n - 1])
    return ans

if __name__ == '__main__':
#    print(addParenthesis('5-8+7*4-8+9'))
    print(addParenthesis(input()))
