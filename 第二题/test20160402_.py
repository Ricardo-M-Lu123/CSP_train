#核心思想：找到可以降落的最深处对应的4*4开始位置
def read_board():
    return read_mtx(15, 10)

def read_block():
    return read_mtx(4, 4)

def read_mtx(m, n):
    mtx = []
    for r in range(m):
        col = input().split()
        mtx.append(col)
    return mtx

game_board = read_board()
# print_board(game_board)
block_pattern = read_block()
# print_block(block_pattern)

start_column = int(input()) - 1
# print("start:", start_column)
start_row = 0 #(start_row, start_column)是板块图案的基准点
# 板块图案block_pattern叠加到方块图game_board上，基准位置是left_up，是合法的吗？
def is_ok(game_board, block_pattern, left_up):
    for r in range(4):
        for c in range(4):
            if block_pattern[r][c] == '1':
                if left_up[0] + r >= 15:
                    return False
                if game_board[left_up[0] + r][left_up[1] + c] == '1':
                    return False

    return True

while is_ok(game_board, block_pattern, (start_row, start_column)):
    start_row += 1  #下落一行

start_row -= 1  #回退到本次下落之前
for r in range(4) :
    for c in range(4):
        if block_pattern[r][c] == '1':
            game_board[start_row + r][start_column + c] = '1'

for r in range(15):
    print(' '.join(game_board[r]))
