# https://programmers.co.kr/learn/courses/30/lessons/84021
def solution(game_board, table):
    n = len(game_board)
    visited = [[False for _ in range(n)] for _ in range(n)]
    empty_boards = []
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                one = dfs(i, j, game_board, visited, n, 0, [])
                if one:
                    empty_boards.append(one)
    visited = [[False for _ in range(n)] for _ in range(n)]
    puzzles = []
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                one = dfs(i, j, table, visited, n, 1, [])
                if one:
                    puzzles.append(one)
    answer = 0
    used_empty_board = [False for _ in range(len(empty_boards))]
    used_puzzle = [False for _ in range(len(puzzles))]
    for ei, empty_board in enumerate(empty_boards):
        for pi, puzzle in enumerate(puzzles):
            if not used_puzzle[pi] and not used_empty_board[ei]:
                rotated_puzzle = puzzle
                for _ in range(4):
                    rotated_puzzle = rotate(rotated_puzzle)
                    if same(rotated_puzzle, empty_board):
                        answer += len(puzzle)
                        used_puzzle[pi] = True
                        used_empty_board[ei] = True
                        break
    return answer


def dfs(x, y, board, visited, n, target, one):
    if visited[x][y]:
        return
    visited[x][y] = True
    one.append((x, y))
    for newX, newY in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
        if 0 <= newX < n and 0 <= newY < n and not visited[newX][newY] and board[newX][newY] == target:
            dfs(newX, newY, board, visited, n, target, one)
    return one


def rotate(p):
    return [(-y, x) for x, y in p]


def same(p1, p2):
    p1.sort()
    p2.sort()
    p1 = [(x - p1[0][0], y - p1[0][1]) for x, y in p1]
    p2 = [(x - p2[0][0], y - p2[0][1]) for x, y in p2]
    return p1 == p2


if __name__ == "__main__":
    print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 0]],
                   [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
                    [0, 1, 0, 0, 0, 0]]))  # Expect 14
    print(solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]]))  # Expect 0
