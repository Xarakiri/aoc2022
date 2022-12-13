from functools import cmp_to_key

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

seen = {}
arr = [[[2]], [[6]]]
for ind, line in enumerate(inp, 1):
    a, b = list(map(eval, line.split('\n')))
    arr.append(a)
    arr.append(b)

arr.sort(key=cmp_to_key(comp), reverse=True)
print((1 + arr.index([[2]])) * (1 + arr.index([[6]])))
