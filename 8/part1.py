from typing import List


def solve(m: List[List[int]]):
    visible = 0
    n_row = len(m)
    n_col = len(m[0])
    for r in range(n_row):
        for c in range(n_col):
            if r % (n_row - 1) == 0 or c % (n_col - 1) == 0:  # edge case
                visible += 1
                continue
            cur_height = m[r][c]
            column = [m[i][c] for i in range(n_row)]
            if all([x < cur_height for x in m[r][:c]]) or all([x < cur_height for x in m[r][c+1:]]):
                visible += 1
            elif all([x < cur_height for x in column[:r]]) or all([x < cur_height for x in column[r+1:]]):
                visible += 1
            else:
                continue
    return visible


matrix = [[int(j) for j in i.rstrip('\n')] for i in open('./input').readlines()]

answer = solve(matrix)
print('part 1 = ', answer)
