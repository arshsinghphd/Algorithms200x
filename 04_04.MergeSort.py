def merge(arr1, arr2):
    merged_arr = []
    while arr1 and arr2:
        if arr1[0] >= arr2[0]:
            a = arr2.pop(0)
            # a = arr1.pop(0) # for reverse sort
            merged_arr += [a]
        else:
            a = arr1.pop(0)
            # a = arr2.pop(0) # for reverse sort
            merged_arr += [a]
    if arr1:
        merged_arr += arr1
    if arr2:
        merged_arr += arr2
    return merged_arr
    
    
def mergeSort(elements): # make sure not to send empty list
    # Block: DIVIDE
    if len(elements) == 1: # if only one element
        return elements
    # no need to write else
    mid = (len(elements)) // 2
    l_elements = mergeSort(elements[: mid])
    r_elements = mergeSort(elements[mid :])
    sorted_elements = merge(l_elements, r_elements)
    return sorted_elements

if __name__ == '__main__':
    len_n = int(input())
    #elements = list(map(int,input().strip().split()))
    elements = sorted(list(range(1,len_n+1)),reverse=True)
    assert len_n == len(elements)
    left = 0
    right = len_n
    print(mergeSort(elements))
        
