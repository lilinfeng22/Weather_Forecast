from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMessageBox, QLabel
from PyQt5.QtCore import pyqtSlot, QSettings
from PyQt5.QtGui import QIcon

class InputWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(" ")
        self.setWindowIcon(QIcon(':/天气符号/素材/下雨.png'))
        self.setGeometry(200, 200, 250, 100)
        self.input_box = QLineEdit(self)
        self.input_box.move(20, 30)
        self.input_box.resize(200, 30)
        self.input_box.returnPressed.connect(self.save_input)

        # 设置输入框样式
        self.input_box.setStyleSheet("QLineEdit { border: 1px solid gray; border-radius: 5px; padding: 2px }")

        # 添加提示文本
        self.label = QLabel("输入查询城市(加载较慢，请稍等)", self)
        self.label.move(20, 10)

        self.show()

    @pyqtSlot()
    def save_input(self):
        input_value = self.input_box.text()
        settings = QSettings('MyCompany', 'MyApp')
        settings.setValue('input_value', input_value)

        # 弹出消息对话框
        #QMessageBox.information(self, "提示", "输入已保存")

        # 关闭窗口
        self.close()
import img_rc
app = QApplication([])
input_window = InputWindow()
app.exec_()
