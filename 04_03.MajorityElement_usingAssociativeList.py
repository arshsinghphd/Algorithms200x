def majority_element(coll):
    '''
    coll -> list of length n
    returns:
        1 if any element is present more than n/2 times
        0 if no such element
    '''
    counts = {}
    for i in range(len(coll)):
        if coll[i] not in counts.keys():
            counts[coll[i]] = 1
        else:
            counts[coll[i]] += 1

    for i in counts:
        if counts[i] >= len(coll)/2:
            return 1

    return 0

if __name__=='__main__':
    coll = list(map(int, input().split()))
    print(majority_element(coll))
