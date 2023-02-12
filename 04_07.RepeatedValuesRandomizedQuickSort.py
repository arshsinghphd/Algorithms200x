import sys
import random

def partition3(elements, left, right):
    j = left
    pivot = elements[left]
    for i in range(left+1, right+1):
        if elements[i] < pivot:
            j += 1
            elements[i], elements[j] = elements[j], elements[i]
    elements[left], elements[j] = elements[j], elements[left]

    # for repeated elements
    k = j
    for i in range(j + 1, right + 1):
        if elements[i] == pivot:
            k += 1
            elements[i], elements[k] = elements[k], elements[i]
    return j, k
        
def randomized_quick_sort(elements, left, right):
    if left > right:
        return
    r = random.randint(left,right)
    elements[r], elements[left] = elements[left], elements[r]
    
    j, k = partition3(elements, left, right)
    randomized_quick_sort(elements, left, j - 1)
    randomized_quick_sort(elements, k + 1, right)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
