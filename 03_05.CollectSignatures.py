from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    global ops
    test = segments[0].end
    ops += [test]
    while segments:
        if segments[0].start <= test:
            segments.pop(0)
        else:
            optimal_points(segments)
    return ops

if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    segments=sorted(segments, key=lambda s: s.end)
    ops = []
    points = optimal_points(segments)
    print(len(points))
    print(*points)
