def neigh4(x, y, H, W):
    for nx, ny in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
        if 0 <= nx < H and 0 <= ny < W:
            yield (nx, ny)


input = [i.strip() for i in open("./input", "r").readlines()]

grid = input[:]
H = len(grid)
W = len(grid[0])


def is_good(a, b):
    return ord(b.replace("E", "z")) - ord(a.replace("S", "a")) <= 1


for src_char in "S", "Sa":  # Part 1, then 2
    queue = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] in src_char:
                queue.append((0, i, j))
    # breadh-first search for shortest path
    seen = set()
    for m, x, y in queue:
        if grid[x][y] == "E":
            print(m)
            break
        for nx, ny in neigh4(x, y, H, W):
            if is_good(grid[x][y], grid[nx][ny]) and (nx, ny) not in seen:
                seen.add((nx, ny))
                queue.append((m + 1, nx, ny))
