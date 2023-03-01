from sys import stdin

def refills(location, distance, tank, stops):
    if location + tank >= distance:
        return 0
    if not stops or stops[0] - location > tank:
        return float('inf')
    last_stop = location
    while stops and stops[0] - location <= tank:
        last_stop = stops[0]
        stops.pop(0)
    return 1 + refills(last_stop, distance, tank, stops)

if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    num_refills = refills(0, d, m, stops)
    print(-1 if num_refills == float('inf') else num_refills)
