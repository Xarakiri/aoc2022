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


pos_lines = []
neg_lines = []

for i, s in enumerate(sensors_beacons):
    d = dists[i]
    neg_lines.extend([s[0][0] + s[0][1] - d, s[0][0] + s[0][1] + d])
    pos_lines.extend([s[0][0] - s[0][1] - d, s[0][0] - s[0][1] + d])


pos = None
neg = None

for i in range(2 * len(sensors_beacons)):
    for j in range(i + 1, 2 * len(sensors_beacons)):
        a, b = pos_lines[i], pos_lines[j]

        if abs(a - b) == 2:
            pos = min(a, b) + 1
        
        a, b = neg_lines[i], neg_lines[j]

        if abs(a - b) == 2:
            neg = min(a, b) + 1


x, y = (pos + neg) // 2, (neg - pos) // 2
ans = x * 4_000_000 + y
print('part 2 = ', ans)
