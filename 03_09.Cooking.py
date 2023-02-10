from sys import stdin
from collections import namedtuple

Dish = namedtuple('Dish', 'c f')

def cooking(dishes):
    '''
    Input: You are cooking n dishes for a dinner. For the i-th dish, it takes
    ci​ minutes to cook it, after which it stays fresh for fi minutes.

    Input format: The first line of the input contains the number n of dishes.
    The i-th of the next n lines contain the time ci to cook the i-th dish and
    the time fi​ it stays fresh.
    
    Output: Is there an order of cooking these n dishes that ensures that at
    some point all of them are fresh? Assume that you cook them one by one
    and cannot parallelize your work.
    
    Output format. “Yes” if there is an order of cooking these n dishes that
    ensures that at some point all of them are fresh, and “No” otherwise.
    '''
    ans = "No"

    for _ in dishes:
        print(dishes)
        # test this sequence
        for i in range(len(dishes)-1): 
            # find sum of cook time of all subsequent dishes
            cooktime = 0
            for j in range(i+1, len(dishes)):
                cooktime += dishes[j].c
            if dishes[i].f >= cooktime:
                ans = "Yes"
                continue
            else:
                ans = "No"
                # break this loop, we need to test another sequence
                dishes[i], dishes[i+1] = dishes[i+1], dishes[i]
                break      
        if ans == "Yes":
            break
        else:
            continue

    return ans
    
if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    dishes = list(map(lambda x: Dish(x[0], x[1]), zip(data[::2], data[1::2])))
    dishes.sort(key= lambda x: x.f, reverse=True)
    ans = ''
    print(cooking(dishes))
