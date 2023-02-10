from sys import stdin

def min_refills(location, d, m, stops):
    '''    
    Input format.  The first line contains an integer d. The second line
    contains an integer m. The third line specifies an integer n. Finally, the
    last line contains integers stop_1,stop_2,…,stop_n.

    Output format.  The minimum number of refills needed. If it is not possible
    to reach the destination, output −1.
    '''
    if location + m >= d:
        return 0
    
    if len(stops) == 0 or (stops[0] - location) > m:
        return -1

    lastStop = location

    while len(stops) > 0 and (stops[0] - location) <= m:
        lastStop = stops[0]
        stops.pop(0)
        
    return 1 + min_refills(lastStop, d, m, stops)

if __name__=='__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    location = 0
    print(min_refills(location, d, m, stops))
