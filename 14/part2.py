import re


def gi(line):
    #(?:(?<!\d)-)?\d+
    return list(map(int, re.findall(r"-?\d+", line)))


class Point(tuple):
    def __add__(self, other):
        return Point(x + y for x, y in zip(self, other))
    
    def __sub__(self, other):
        return Point(x - y for x, y in zip(self, other))


class Segment:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
    
    def contains(self, v: Point) -> bool:
        return min(self.start[0], self.end[0]) <= v[0] and v[0] <= max(self.start[0], self.end[0]) and \
               min(self.start[1], self.end[1]) <= v[1] and v[1] <= max(self.start[1], self.end[1])


def contains_in_cave(cave, value) -> bool:
    for seg in cave:
        if seg.contains(value):
            return True
    return False


def hit_the_bottom(threshold: int, bottom: Point) -> bool:
    return bottom[1] == threshold + 2


cave = []
with open('input', 'r') as f:
    for l in f.readlines():
        l = l.rstrip('\n')

        points = [gi(i) for i in l.split(" -> ")]
        point = points.pop(0)
        start = Point((point[0], point[1]))
        while points:
            point = points.pop(0)
            end = Point((point[0], point[1]))
            segment = Segment(start, end)
            cave.append(segment)
            start = end

sand_source = Point((500, 0))
threshold = max([max(i.start[1], i.end[1]) for i in cave])


sand = set()
i = 0
while True:
    i += 1
    if i % 1000 == 0:
        print(i)
    new_grain = sand_source
    while True:
        bottom = new_grain + Point((0, 1))
        if not contains_in_cave(cave, bottom) and bottom not in sand and not hit_the_bottom(threshold, bottom):
            new_grain = bottom
            continue
        
        bottom_left = new_grain + Point((-1, 1))
        if not contains_in_cave(cave, bottom_left) and bottom_left not in sand and not hit_the_bottom(threshold, bottom_left):
            new_grain = bottom_left
            continue
        
        bottom_right = new_grain + Point((1, 1))
        if not contains_in_cave(cave, bottom_right) and bottom_right not in sand and not hit_the_bottom(threshold, bottom_right):
            new_grain = bottom_right
            continue
        break

    sand.add(new_grain)
    if new_grain[0] == sand_source[0] and new_grain[1] == sand_source[1]:
        break

print(len(sand))
