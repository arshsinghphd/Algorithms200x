from sys import stdin
from bisect import bisect_left, bisect_right

def pointsInSegments(starts, ends, points):
    starts, ends = sorted(starts), sorted(ends)
    count = [len(starts)] * len(points)
    for index, point in enumerate(points):
        not_covered = bisect_left(ends, point)
        not_covered += len(starts) - bisect_right(starts, point)
        count[index] -= not_covered
    return count
    
if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]

    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]
    
    output_count = pointsInSegments(input_starts, input_ends, input_points)
    print(*output_count)
    
