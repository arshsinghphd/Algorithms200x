def max_pairwise_product(numbers):
    n = len(numbers)
    a=max(numbers)
    idx_a=numbers.index(a)
    numbers.pop(idx_a)
    b=max(numbers)
    return a*b

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
