def majority_element(elements, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return elements[left]
    middle = (left + right) // 2
    x = majority_element(elements, left, middle)
    if 2 * elements[left:right].count(x) > right - left:
        return x
    x = majority_element(elements, middle, right)
    if 2 * elements[left:right].count(x) > right - left:
        return x
    return -1


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    if majority_element(input_elements, 0, input_n) != -1:
        print(1)
    else:
        print(0)
