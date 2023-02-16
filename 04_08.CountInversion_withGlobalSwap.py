import random
random.seed(42)
from itertools import combinations

def merge(arr1, arr2):
    global swaps
    
    merged_arr = []
    while arr1 and arr2:
        if arr1[0] > arr2[0]:
            a = arr2.pop(0)
            merged_arr += [a]
            swaps += len(arr1)
        else:
            a = arr1.pop(0)
            merged_arr += [a]      
    if arr1:
        merged_arr += arr1

    if arr2:
        merged_arr += arr2
        
    return merged_arr, swaps
    
def mergeSort(elements): # make sure not to send empty list
    global swaps
    
    if len(elements) == 1: # if only one element
        return elements
    
    mid = (len(elements)) // 2
    l_elements = mergeSort(elements[: mid])
    r_elements = mergeSort(elements[mid :])
    sorted_elements, swaps = merge(l_elements, r_elements)
    return sorted_elements

def countInversions(arr):
    global swaps
    swaps = 0
    mergeSort(arr)
    return swaps
    
def bruteForce(arr):
    ans = 0
    len_n = len(arr)
##    for i in range(len_n):
##        for j in range(i,len_n):
##            if arr[i] > arr[j]:
##                ans += 1
    for i, j in combinations(range(len(arr)), 2):
        if arr[i] > arr[j]:
            ans += 1
    return ans

if __name__=='__main__':
##    arr = [1, 3, 2]
    arr = [1, 6, 3, 4, 5, 2, 2, 7, 8, 9, 10, 2]
##    arr = [3, 2, 5, 9, 4]
##    arr = [2, 3, 9, 2, 9]
    print(bruteForce(arr))
    len_n = len(arr)
    print(countInversions(arr))
    
