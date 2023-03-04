
def countReps(array, q):
    '''
    Input: A sorted integer array (possibly with duplicates) and an integer q.
    Output: The number of times q appears in the array.
    '''
    if q < array[0] or q > array[-1]:
        return 0
    
    else:
        start = 0
        end = len(array) - 1
        mid = (start + end) // 2
        
        while end >= start:
            mid = (start + end) // 2
            if array[mid] == q:
                i = mid
                j = mid
                while array[i - 1] == q:
                    i -= 1
                try:
                    while array[j + 1] == q:
                        j += 1    
                except:
                    None
                return j - i + 1
            elif array[mid] > q:
                end = mid - 1
            else:
                start = mid + 1
        return 0
    
if __name__ == '__main__':
    array = [1,2,2,2,3,4,5,6,7]
    
    for q in array:
        print(q, end = ' ')
        print(countReps(array, q))
        
