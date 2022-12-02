total = 0
d = {
    'A': 1,
    'B': 2,
    'C': 3,
}
switch = {
    'A': ['B', 'C'],
    'B': ['C', 'A'],
    'C': ['A', 'B']
}
with open('input2', 'r') as f:
    for l in f.readlines():
        a, b = l.strip().split()

        # lose
        if b == 'X':
            b = switch[a][1]
        elif b == 'Y': # draw
            total += 3
            b = a
        else: # win
            total += 6
            b = switch[a][0]
        total += d[b]
    

print(total)
