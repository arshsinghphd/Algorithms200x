def lcs3(a, b, c, na, nb, nc):
    D = [[['' for _ in range(nc + 1)]
          for _ in range(nb + 1)]
         for _ in range(na + 1)]
    for k in range(nc + 1):
        for j in range(nb + 1):
            for i in range(na + 1):
                if i == 0 or j == 0 or k == 0:
                    D[i][j][k] = 0
                else:
                    D[i][j][k] = max(D[i - 1][j][k],
                                     D[i][j - 1][k],
                                     D[i][j][k - 1],
                                     D[i - 1][j - 1][k - 1]
                                     + 1*(a[i - 1] == b[j - 1] == c[k - 1])
                                     )
    return D[na][nb][nc]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c, n, m, q))


##print(lcs3([2,7,2,5,3], [2,5,2,3], [2, 5, 3],
##           5, 4, 3))
##print(lcs3([8, 2, 3, 1, 7], [8, 2, 1, 3, 8 , 10 , 7], [6, 8, 3, 1, 4, 7],
##           5, 7, 6))
##print(lcs3([1, 2, 3], [2, 1, 3], [1, 3, 5],
##           3, 3, 3))

