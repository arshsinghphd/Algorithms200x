import sys

def fillSackRecursively(w, bars, i, pack):
    if (w, i) not in pack:
    #   if reached end of bars and the bag is full    
        if i == 0 and w == 0:
            pack[(w, i)] = True
        
    #   if reached end of bars, and bag is not full
        elif i == 0 and w > 0:
            pack[(w, i)] = False
        
    #   skip if bar is greater than capacity left.
        elif i > 0 and bars[i - 1] > w: 
            pack[(w, i)] = fillSackRecursively(w, bars, i - 1, pack)
        
    #   i > 0 and bars[i - 1] <= capacity left
        else:
    #       skip or select the ith bar
            pack[(w, i)] = fillSackRecursively(w, bars, i - 1, pack) \
                         or fillSackRecursively(w - bars[i - 1],
                                                bars, i - 1, pack)

    return pack[(w, i)]

if __name__ == '__main__':
    input = sys.stdin.read()
    cap, n, *bars = list(map(int, input.split()))
    pack = {}
    for s in range(cap, -1, -1):
        if fillSackRecursively(s, bars, n, pack):
            print(s)
            break
