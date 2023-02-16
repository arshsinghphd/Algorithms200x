from sys import stdin
from collections import namedtuple

Dish = namedtuple('Dish', 'c f')

def cooking(dishes, cooktime = 0):
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
    if len(dishes) <= 1:
        return 1
    else:
        cooktime += dishes[0].c
        dishes.pop(0)
        print(dishes[0].f, cooktime)
        if dishes[0].f >= cooktime:
            return 1*cooking(dishes, cooktime)
        else:
            return 0
        
if __name__ == '__main__':
##    input = stdin.read()
##    n, *data = map(int, input.split())
##    dishes = list(map(lambda x: Dish(x[0], x[1]), zip(data[::2], data[1::2])))
    dishes = [Dish(2,3), Dish(2,2), Dish(2,1)]    
    dishes.sort(key= lambda x: x.f + x.c)
    if cooking(dishes) == 0:
        print('No')
    else:
        print('Yes')
