with open('input', 'r') as f:
    l = f.readline().strip()

for i in range(0, len(l)):
    if len(set(l[i:i+4])) == 4:
        print(i + 4)
        break
