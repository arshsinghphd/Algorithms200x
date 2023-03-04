def change(money):
    # write your code here
    table = [float('inf') for _ in range(money + 1)]
    table[0] = 0
    
    for m in range(1, money + 1):
        for c in [1,3,4]:
            if c <= m:
                table[m] = min(table[m], 1 + table[m - c])
    return table[money]

if __name__ == '__main__':
    m = int(input())
    print(change(m))