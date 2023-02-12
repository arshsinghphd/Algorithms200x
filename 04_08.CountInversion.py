def merge(left_array, right_array):
    merged_array = []
    split_inv = 0
    
    while left_array and right_array:
        # if element from right is smaller
        if left_array[0] > right_array[0]: 
            merged_array.append(right_array.pop(0))
            split_inv += len(left_array)
            # it moves len(left) place to the left
        else:
            merged_array.append(left_array.pop(0))

    merged_array.extend(left_array)
    merged_array.extend(right_array)

    return merged_array, split_inv

def sort_CountInversions(array):
    if len(array) == 1:
        return array, 0
    left_array = array[: len(array) //2 ]
    right_array = array[len(array) // 2 :]
    
    left_array, left_inv = sort_CountInversions(left_array)
    right_array, right_inv = sort_CountInversions(right_array)

    array, split_inv = merge(left_array, right_array)

    return array, left_inv + right_inv + split_inv
    
if __name__=='__main__':
    array = [1, 4, 3, 2]
    array, inv = sort_CountInversions(array)
    print(inv)



