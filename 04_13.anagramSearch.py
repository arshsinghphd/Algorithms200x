def test(listIdx):
    i = listIdx[len(listIdx) - 1]
    j = listIdx[len(listIdx) - 2]
    s1 = [c for c in a[i]].sort()
    s2 = [c for c in a[j]].sort()
    if s1 == s2:
        return 1
    else:
        return 0
    
def anagrams(a):
    '''
    Tests for anagrams in an array of strings
    Returns true as soon as one is found
    '''
    # convert the strings in a to sum of ord values and store them in b.
    # if values in b are same, then sort the string at these index values
    b = [0 for s in a]
    dups = {}
    for i, s in enumerate(a):
        for c in s:
            b[i] += ord(c)
        if b[i] not in dups:
            dups[b[i]] = [i]
        else:
            dups[b[i]].append(i)
            # test the elements of a at the two indices stored at the
            # end of the list in dups[b[i]]
            if test(dups[b[i]]):
                return True
    return False

a = ['aa','ba','bc','bb','aa']
print(anagrams(a))
        
