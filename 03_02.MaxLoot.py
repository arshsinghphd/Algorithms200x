from sys import stdin

def optimal_value(capacity, weights, values):
    '''
    Input format:  The first line of the input contains the number n of
    compounds and the capacity W of a backpack. The next n lines define the
    costs and weights of the compounds.

    Output format:  Output the maximum value of compounds that fit into the
    backpack.
    '''

    value = 0
    dict_ = {}
    n_comps = len(weights)
    
    for i in range(n_comps):
        dict_[values[i]/weights[i]] = values[i], weights[i]

    for comp in sorted(dict_.keys(), reverse=True):

        if capacity > dict_[comp][1]:
            value += dict_[comp][0]
            capacity -= dict_[comp][1]

        else:
            value += comp * capacity
            capacity = 0
            
    return value

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
