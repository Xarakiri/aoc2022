total = 0
d = {
    'A': 1,
    'B': 2,
    'C': 3,
}
switch = {
    'X': 'A', 'Y': 'B', 'Z': 'C'
}
with open('input', 'r') as f:
    for l in f.readlines():
        a, b = l.strip().split()
        b = switch[b]

        if a == b:
            total += 3
        if a == 'A' and b == 'B':
            total += 6
        if a == 'B' and b == 'C':
            total += 6
        if a == 'C' and b == 'A':
            total += 6
        total += d[b]
    

print(total)
