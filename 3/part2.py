import string
total = 0
with open('input', 'r') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        s1 = set(lines[i].strip())
        s2 = set(lines[i+1].strip())
        s3 = set(lines[i+2].strip())

        ch = (s1 & s2 & s3).pop()
        if "a" <= ch <= "z":
            total += string.ascii_lowercase.index(ch) + 1
        else:
            total += ord(ch) - 38
print(total)
