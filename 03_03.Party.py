def makeGroups(ages):
    '''
    Given: a list of ages of children. Group children such that they are not
    more than 2 years apart.
    
    Return minimum number of such groups. 
    '''
    n_kids = len(ages)
    ages.sort()
    low = ages[0]
    n_groups = 1
    for i in range(n_kids):
        if ages[i] > low + 2:
            n_groups += 1
            low = ages[i]
    return n_groups

if __name__ == '__main__':
    ages = list(map(int,input().split()))
    print(makeGroups(ages))
