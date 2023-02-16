from collections import namedtuple
from itertools import combinations
from math import sqrt

Point = namedtuple('Point', 'x y')

def distance(p, q):
    return (p.x - q.x)**2 + (p.y - q.y)**2

def minDistanceSquared(points):
    if len(points) <= 3:
        d = 10**9
        for p, q in combinations(points, 2):
            d = min(d, distance(p, q))
        return d

    else:
        points = sorted(points, key = lambda p: p.x)
        mid_i = len(points) // 2
        mid_x = points[mid_i].x

        d_l = minDistanceSquared(points[:mid_i])
        d_r = minDistanceSquared(points[mid_i:])
        d = min(d_l, d_r)

        points_prime = [p for p in points if (p.x -mid_x)**2 <= d]
        points_prime = sorted(points_prime, key = lambda p: p.y)
        for i in range(len(points_prime)):
            j = i + 1
            while j < len(points_prime) and \
                  distance(points_prime[i], points_prime[j]) < d:
                d = distance(points_prime[i], points_prime[j])
                j += 1
    return d
    
if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)
    print("{0:.9f}".format(sqrt(minDistanceSquared(input_points))))
