def duplicateSearch(a):
    f = {}
    for e in a:
        if e not in f:
            f[e] = 1
        else:
            f[e] += 1

    return [(e, f[e]) for e in f if f[e] > 1]        
    
if __name__ == '__main__':
    a = [1, 1, 2, 3, 3, 4, 5]
    print(duplicateSearchDQ(a))
