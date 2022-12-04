total = 0

with open('input', 'r') as f:
    for l in f. readlines():
        l = l.strip()
        pair1, pair2 = l.split(',')

        p1, p2 = map(int, pair1.split('-'))
        p3, p4 = map(int, pair2.split('-'))

        if p2 >= p4 and p1 <= p3:
            total += 1
        elif p3 <= p1 and p4 >= p2:
            total += 1

print(total)
