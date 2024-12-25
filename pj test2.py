import sys
import numpy as np
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QVBoxLayout

# 棋盤大小
BOARD_SIZE = 15

class GomokuGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("五子棋")
        self.resize(600, 600)

        # 初始化棋盤，0表示空，1表示玩家1（X），-1表示玩家2（O）
        self.board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
        self.current_player = 1  # 玩家1（X）先手

        # 設置主窗口
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        # 設置標籤顯示當前玩家
        self.label = QLabel("玩家 1 (X) 的回合", self)
        
        # 設置棋盤佈局
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(1)  # 按鈕間隔

        # 添加棋盤按鈕
        self.buttons = {}
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                button = QPushButton("", self)
                button.setFixedSize(40, 40)
                button.setStyleSheet("background-color: white; border: 1px solid black;")
                button.clicked.connect(lambda checked, r=row, c=col: self.make_move(r, c))
                self.grid_layout.addWidget(button, row, col)
                self.buttons[(row, col)] = button

        # 設置佈局
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(self.grid_layout)
        self.main_widget.setLayout(layout)

    def make_move(self, row, col):
        """處理玩家的棋步"""
        if self.board[row][col] != 0:
            return  # 已經有棋子，無法再次下棋
        
        # 根據當前玩家在棋盤上放置棋子
        self.board[row][col] = self.current_player
        button = self.buttons[(row, col)]

        if self.current_player == 1:
            button.setText("X")
            button.setStyleSheet("color: red; background-color: white; border: 1px solid black;")
            self.label.setText("玩家 2 (O) 的回合")
        else:
            button.setText("O")
            button.setStyleSheet("color: blue; background-color: white; border: 1px solid black;")
            self.label.setText("玩家 1 (X) 的回合")

        # 檢查是否有玩家獲勝
        if self.check_win(self.current_player):
            self.label.setText(f"玩家 {self.current_player} 獲勝！")
            self.disable_all_buttons()
            return
        
        # 換下棋方
        self.current_player = -self.current_player

    def check_win(self, player):
        """檢查是否有玩家獲勝"""
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.board[i][j] == player:
                    # 檢查水平方向
                    if j + 4 < BOARD_SIZE and all(self.board[i][j+k] == player for k in range(5)):
                        return True
                    # 檢查垂直方向
                    if i + 4 < BOARD_SIZE and all(self.board[i+k][j] == player for k in range(5)):
                        return True
                    # 檢查右下對角線
                    if i + 4 < BOARD_SIZE and j + 4 < BOARD_SIZE and all(self.board[i+k][j+k] == player for k in range(5)):
                        return True
                    # 檢查左下對角線
                    if i + 4 < BOARD_SIZE and j - 4 >= 0 and all(self.board[i+k][j-k] == player for k in range(5)):
                        return True
        return False

    def disable_all_buttons(self):
        """禁用所有棋盤按鈕"""
        for button in self.buttons.values():
            button.setEnabled(False)

# 主程式入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GomokuGame()
    window.show()
    sys.exit(app.exec())
