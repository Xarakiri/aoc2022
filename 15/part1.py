import re


class Point(tuple):
    def __add__(self, other):
        return Point(x + y for x, y in zip(self, other))
    
    def __sub__(self, other):
        return Point(x - y for x, y in zip(self, other))
    
    def norm(self):
        return sum([abs(x) for x in self])

def gi(line):
    # (?:(?<!\d)-)?\d+
    return list(map(int, re.findall(r"-?\d+", line)))

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


sensors_beacons = [(Point(gi(i)[:2]), Point(gi(i)[2:])) for i in open('./input').readlines()]

dists = []

for i in range(len(sensors_beacons)):
    dists.append(dist(sensors_beacons[i][0], sensors_beacons[i][1]))


Y = 2_000_000

intervals = []

for i, s in enumerate(sensors_beacons):
    dx = dists[i] - abs(s[0][1] - Y)

    if dx <= 0:
        continue

    intervals.append((s[0][0] - dx, s[0][0] + dx))


# interval overlap
allowed_x = []
for v in sensors_beacons:
    bx, by = v[1]
    if by == Y:
        allowed_x.append(bx)


min_x = min([i[0] for i in intervals])
max_x = max([i[1] for i in intervals])

ans = 0
for x in range(min_x, max_x + 1):
    if x in allowed_x:
        continue

    for left, right in intervals:
        if left <= x <= right:
            ans += 1
            break

print('part 1 = ', ans)
