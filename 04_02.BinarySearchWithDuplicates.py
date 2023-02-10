def binary_search(keys, query):
    ans = -1
    min_index, max_index = 0, len(keys) - 1
    while max_index >= min_index:
        mid_index = (min_index + max_index) // 2
        if keys[mid_index] == query:
            max_index = mid_index - 1
            ans = mid_index
        elif keys[mid_index] < query:
            min_index = mid_index + 1
        else:
            max_index = mid_index - 1
    return ans

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
