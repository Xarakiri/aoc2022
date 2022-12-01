answer = []

with open('input', 'r') as f:
    current = 0
    for l in f.readlines():
        if l == '\n':
            answer.append(current)
            current = 0
        else:
            current += int(l)

print(sum(sorted(answer, key=lambda x: -x)[:3]))
