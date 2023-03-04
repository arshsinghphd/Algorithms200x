from statistics import median

def medianSortedSlow(a1, a2):
    merged = []
    while a1 and a2:
        if a1[0] > a2[0]:
            merged.append(a2.pop(0))
        else:
            merged.append(a1.pop(0))
    if a1:
        merged.extend(a1)
    if a2:
        merged.extend(a2)
    n = len(merged)
    if n % 2 == 0:
        return (merged[n//2] + merged[n//2 - 1]) / 2
    else:
        return (merged[n//2])

def medianSorted(a1, a2):
    n = len(a2)
    mid = n // 2
    if n == 1:
        print('1')
        return (a1[0] + a2[0]) / 2

    if n == 2:
        print('2')
        merged = a1 + a2
        return median(merged)
    
    # even n
    elif n % 2 == 0:
        print('even')
        if median(a1) < median(a2):
            return medianSorted(a1[mid - 1:], a2[:mid + 1])
        else:
            return medianSorted(a2[mid - 1:], a1[:mid + 1])

    # odd n
    else:
        print('odd')
        if a1[mid] < a2[mid]:
            return medianSorted(a1[mid:], a2[:mid + 1])
        else:
            return medianSorted(a2[mid:], a1[:mid + 1])
        
if __name__ == '__main__':
    a1 = [6, 6, 6, 6, 6, 6, 6, 6]
    a2 = [8, 8, 8, 8, 8, 8, 8, 8]
    merged = a1 + a2
    print(medianSorted(a1, a2), median(merged))
