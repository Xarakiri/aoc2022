answer = 0

with open('input', 'r') as f:
    current = 0
    for l in f.readlines():
        if l == '\n':
            answer = max(answer, current)
            current = 0
        else:
            current += int(l)

print(answer)
