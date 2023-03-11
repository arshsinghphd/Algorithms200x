def coin_game(a):
    '''
    GIVEN:
    An array 'a' with even number of positive integers.
    Two players play a game described as following.

    GAME:
    Two players will play to take one of the either ends of the array.
    Each player score is the sum of integers they picked.
    Each player wants to maximize their final score.
    All this information is public knowledge.
    
    RETURN:
    Maximum possible score for first player
    '''
    table = {}

    for i in range(len(a)): # base case k = 1
        table[(i, 2)] = max(a[i : i + 2])

    for k in range(2, len(a)//2 + 1):
        for i in range(len(a) - 2 * k + 1):
            if (i, 2 * k) not in table:
                l = a[i] + min(table[(i + 2, 2 * k  - 2)],
                               table[(i + 1, 2 * k  - 2)])
                r = a[i + 2 * k - 1] + min(table[(i + 1, 2 * k  - 2)],
                                           table[(i, 2 * k  - 2)])
                table[(i, 2 * k)] = max(l, r)

    return(table[(0, len(a))])

def main():
    n = int(input())
    array = list(map(int, input.split()))
    print(coin_game(array))

if __name__ == '__main__':
    main()
