def majority_element(elements, left, right):
    if left == right: # if the list is empty
        return -1
    if left + 1 == right: # only one element left, return it
        return elements[left]
    mid = (left + right) // 2
    x = majority_element(elements, left, mid) # call again for the left side
    if 2*elements[left: right].count(x) > right - left: # if freq of x > n/2
        return x
    x = majority_element(elements, mid, right) # call again for the right side
    if 2*elements[left: right].count(x) > right - left: # if freq of x > n/2
        return x
    return -1

if __name__ == '__main__':
    len_n = int(input())
    elements=list(map(int,input().split()))
    assert len(elements) == len_n
    ans = majority_element(elements, 0, len_n)
    # in case we want to print ans
    if ans == -1:
        print('0 - none')
    else:
        print('1 - yes, majority element is:',ans)
