def compute_operations(n):
    table = [ [0] for _ in range(n + 1)]
    table[0] = []
    table[1] = [1]
    for i in range(2, n+1):
        s1, s2 = float('inf'), float('inf')
        if i % 3 == 0 :
            s1 = 1 + len(table[i // 3])
        if i % 2 == 0:
            s2 = 1 + len(table[i // 2])
        s3 = 1 + len(table[i - 1])
        
        t = min(s1, s2, s3)
        
        if t == s1:
            table[i] = table[i // 3].copy()
        elif t == s2:
            table[i] = table[i // 2].copy()
        else:
            table[i] = table[i - 1].copy()
        table[i].append(i)
    return table

if __name__ == '__main__':
    input_n = int(input())
    table = compute_operations(input_n)
    output_sequence = table[input_n]
    print(len(output_sequence) - 1)
    print(*output_sequence)
