from typing import List


def solve(m: List[List[int]]):
    score = 0
    n_row = len(m)
    n_col = len(m[0])
    for r in range(1, n_row - 1):
        for c in range(1, n_col - 1):
            cur_height = m[r][c]
            column = [m[i][c] for i in range(n_row)]
            left = up = right = bottom = 0
            for i in range(c - 1, -1, -1):
                if m[r][i] < cur_height:
                    left += 1
                elif m[r][i] == cur_height:
                    left += 1
                    break
                else:
                    left += 1
                    break

            for i in range(c + 1, n_col):
                if m[r][i] < cur_height:
                    right += 1
                elif m[r][i] == cur_height:
                    right += 1
                    break
                else:
                    right += 1
                    break

            for i in range(r - 1, -1, -1):
                if column[i] < cur_height:
                    up += 1
                elif column[i] == cur_height:
                    up += 1
                    break
                else:
                    up += 1
                    break

            for i in range(r + 1, n_row):
                if column[i] < cur_height:
                    bottom += 1
                elif column[i] == cur_height:
                    bottom += 1
                    break
                else:
                    bottom += 1
                    break

            score = max(score, left * up * right * bottom)

    return score


matrix = [[int(j) for j in i.rstrip('\n')] for i in open('./input').readlines()]

answer = solve(matrix)
print('part 2 = ', answer)
