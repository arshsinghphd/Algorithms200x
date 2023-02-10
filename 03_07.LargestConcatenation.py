def largest_number(numbers):
    '''
    Largest Concatenate
    Compile the largest number by concatenating the given numbers.
    Input: A sequence of positive integers.
    Output: The largest number that can be obtained by concatenating the given
    integers in some order.
    '''
    for _ in numbers:
        for i in range(len(numbers) - 1):
            if numbers[i] + numbers[i + 1] < numbers[i + 1] + numbers[i]:
                t = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = t
    return int(''.join(numbers))

if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number(input_numbers))

    
