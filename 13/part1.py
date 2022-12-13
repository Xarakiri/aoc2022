def is_list(x):
    return type(x) is list

def is_int(x):
    return type(x) is int

def comp(a, b):
    if is_int(a) and is_int(b):
        return (a < b) - (a > b)
    elif is_list(a) and is_list(b):
        for i, j in zip(a, b):
            k = comp(i, j)
            if k != 0: return k
        return (len(a) < len(b)) - (len(a) > len(b))
    elif is_int(a):
        return comp([a], b)
    else:
        return comp(a, [b])


inp = [x.rstrip() for x in open('./input').read().split('\n\n')]

total = 0
for ind, line in enumerate(inp, 1):
    a, b = list(map(eval, line.split('\n')))
    if comp(a, b) == 1:
        total += ind


print(total)
