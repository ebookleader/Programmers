def solution(board):
    answer = 0
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i][j-1], board[i-1][j-1], board[i-1][j]) + 1
                if board[i][j] > answer:
                    answer = board[i][j]

    # 1행 or 1열에만 1이 있는 경우 or 전부 0인경우
    if answer == 0:
        if 1 in board[0]:
            answer = 1
        else:
            for i in range(len(board)):
                if board[i][0] == 1:
                    answer = 1
                    break
    return answer ** 2

print(solution([[0, 1, 1, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]))