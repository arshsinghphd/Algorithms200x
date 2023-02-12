import random
random.seed(42)

def partition(elements, left, right):
    j = left
    pivot = elements[left]
    for i in range(left+1, right+1): # since we entered right = len_n - 1
        if elements[i] < pivot:
            j += 1
            elements[i], elements[j] = elements[j], elements[i]
    elements[left], elements[j] = elements[j], elements[left]
    return j
        
def quickSort(elements, left, right):
    if left > right:
        return -1
    j = partition(elements, left, right)
    if j - left  < right - j:
        quickSort(elements, left, j - 1)
    else:
        quickSort(elements, j + 1, right)
    
if __name__=='__main__':
    len_n = int(input())
    
    ## use input list
    # elements = list(map, int(input().split()))
    
    # generate a shuffled list of n natural numbers
    elements = list(range(1,len_n+1))
    random.shuffle(elements)
    
    assert len_n == len(elements)
    print(elements)
    quickSort(elements,0,len_n-1)
    # note to avoid OBOB we are entering right = len_n -1
    print(elements)
