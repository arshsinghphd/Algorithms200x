from itertools import product

def split(values):
    v, n = sum(values), len(values)
    if v % 3 != 0:
        return False
    v = v // 3

    table = [[[False for _ in range(v + 1)]
              for _ in range(v + 1)] for _ in range(n + 1)]
    table[0][0][0] = True

    for i in range(1, n + 1):
        for s1, s2 in product(range(v + 1), repeat=2):
            table[i][s1][s2] = table[i - 1][s1][s2]
            if s1 >= values[i - 1]:
                table[i][s1][s2] |= table[i - 1][s1 - values[i - 1]][s2]
            if s2 >= values[i - 1]:
                table[i][s1][s2] |= table[i - 1][s1][s2 - values[i - 1]]

    return table[n][v][v]

if __name__ == '__main__':
    n = input()
    values = list(map(int, input().split()))
    print(1 if split(values) else 0)

