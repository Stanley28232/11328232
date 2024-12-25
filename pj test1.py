import numpy as np

# 棋盤大小
BOARD_SIZE = 15

# 定義棋盤，0表示空格，1表示玩家1（X），-1表示玩家2（O）
board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)

# 打印棋盤
def print_board():
    print("  ", end="")
    for i in range(BOARD_SIZE):
        print(f"{i:2}", end=" ")
    print()
    
    for i in range(BOARD_SIZE):
        print(f"{i:2}", end=" ")
        for j in range(BOARD_SIZE):
            if board[i][j] == 1:
                print(" X", end=" ")
            elif board[i][j] == -1:
                print(" O", end=" ")
            else:
                print(" .", end=" ")
        print()

# 檢查是否有玩家獲勝
def check_win(player):
    # 檢查行、列、對角線
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == player:
                # 檢查水平方向
                if j + 4 < BOARD_SIZE and all(board[i][j+k] == player for k in range(5)):
                    return True
                # 檢查垂直方向
                if i + 4 < BOARD_SIZE and all(board[i+k][j] == player for k in range(5)):
                    return True
                # 檢查右下對角線
                if i + 4 < BOARD_SIZE and j + 4 < BOARD_SIZE and all(board[i+k][j+k] == player for k in range(5)):
                    return True
                # 檢查左下對角線
                if i + 4 < BOARD_SIZE and j - 4 >= 0 and all(board[i+k][j-k] == player for k in range(5)):
                    return True
    return False

# 進行玩家下棋
def make_move(player):
    while True:
        try:
            print(f"玩家 {('X' if player == 1 else 'O')} 走子:")
            row, col = map(int, input("請輸入行列（格式：行 列）：").split())
            if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
                print("位置無效，請重新輸入。")
                continue
            if board[row][col] != 0:
                print("該位置已經有棋子，請重新選擇。")
                continue
            board[row][col] = player
            break
        except ValueError:
            print("輸入無效，請確保輸入格式正確。")

# 主遊戲循環
def main():
    print("五子棋遊戲開始！")
    print("遊戲規則：五個相同的棋子連成一線即獲勝。")
    print_board()

    current_player = 1  # 玩家1（X）先手
    while True:
        make_move(current_player)
        print_board()
        
        # 檢查是否有玩家獲勝
        if check_win(current_player):
            print(f"玩家 {('X' if current_player == 1 else 'O')} 獲勝！")
            break
        
        # 交換玩家
        current_player = -current_player

if __name__ == "__main__":
    main()
