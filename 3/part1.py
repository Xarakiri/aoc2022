import string
total = 0
with open('input', 'r') as f:
    for l in f.readlines():
        l = l.strip()
        mid = len(l) // 2
        p1, p2 = set(l[:mid]), set(l[mid:])
        ch = p1.intersection(p2).pop()

        if "a" <= ch <= "z":
            total += string.ascii_lowercase.index(ch) + 1
        else:
            total += ord(ch) - 38
print(total)
