###這段程式碼展示了一個簡單的 PyQt6 GUI 程式，實現了以下功能：顯示標籤和輸入框。按下按鈕後顯示輸入的文字，並進行空白檢查。清除輸入框與標籤內容。使用垂直佈局管理元件。
from PyQt6.QtWidgets import (
    QApplication, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QWidget, QMessageBox
)
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 輸入與互動")
        self.resize(400, 300)

        # 元件：標籤、輸入框、按鈕
        self.label = QLabel("請輸入文字並點擊按鈕：", self)
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("在這裡輸入...")
        self.display_button = QPushButton("顯示文字", self)
        self.clear_button = QPushButton("清除文字", self)

        # 設定佈局
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.display_button)
        layout.addWidget(self.clear_button)
        self.setLayout(layout)

        # 事件連接
        self.display_button.clicked.connect(self.display_text)
        self.clear_button.clicked.connect(self.clear_text)

    def display_text(self):
        text = self.input_field.text()
        if text.strip():
            self.label.setText(f"您輸入了：{text}")
        else:
            QMessageBox.warning(self, "警告", "輸入欄位為空！")

    def clear_text(self):
        self.input_field.clear()
        self.label.setText("請輸入文字並點擊按鈕：")

# 主程式入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())