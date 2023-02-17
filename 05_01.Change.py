# Uses python3
import sys

def get_change(m):
    '''
    change money using 1, 3, 4
    '''
    coins = [1, 3, 4]
    dict_m = {}
    
    for c in coins: # fill initial values
        dict_m[c] = 1
        
    for amt in range(min(coins), m):
        for c in coins:
            if amt in dict_m:
                if amt + c in dict_m:
                    if dict_m[amt + c] > dict_m[amt] + 1:
                        dict_m[amt + c] = dict_m[amt] + 1
                else:
                    dict_m[amt + c] = dict_m[amt] + 1

    #print(sorted([i for i in zip(dict_m.keys(), dict_m.values())], key=lambda x: x[0]))
        
    return dict_m[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
