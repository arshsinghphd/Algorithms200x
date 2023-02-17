# Uses python3
import sys

def mul3(i):
    return i * 3

def mul2(i):
    return i * 2

def add1(i):
    return i + 1

def optimal_sequence(n):
    list_seq = [[0]]*(n+1)
    list_seq[1] = [1]
    actions = [add1, mul2, mul3]
    for i in range(0,n):
        for action in actions:
            j = action(i)
            if 0 < j <= n:
                if list_seq[j] == [0]:
                    temp = list_seq[i].copy()
                    temp.append(j)
                    list_seq[j] = temp
                elif len(list_seq[j]) > len(list_seq[i]) + 1:
                    temp = list_seq[i].copy()
                    temp.append(j)
                    list_seq[j] = temp
    return list_seq[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
