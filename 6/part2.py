with open('input', 'r') as f:
    l = f.readline().strip()


start = 0
for i in range(0, len(l)):
    if len(set(l[i:i+14])) == 14:
        print(i + 14)
        break
