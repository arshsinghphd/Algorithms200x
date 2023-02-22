def partition3(array):
    if sum(array) % 3 != 0:
        return 0
    else:
        fair_share = sum(array) // 3
        table = {(0, 0): True}
        for i in range(len(array)):
            for (x, y) in table.copy():
                table[(x + array[i], y)] = True
                table[(x, y + array[i])] = True
        if (fair_share, fair_share) in table:
            return 1
        else:
            return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    input = list(map(int, input.split()))
    n = input[0]
    A = input[1:]
    print(partition3(A))

