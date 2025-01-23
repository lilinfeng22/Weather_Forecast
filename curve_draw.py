# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import api_num  # 导入你需要的模块
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox

def showResult(xList, yList, title, xLabel, yLabel):
    plt.figure(figsize=(7.91, 1.91), dpi=100)  # 设置图形大小和分辨率
    plt.ylim( max(yList) + 1, min(yList) - 1)
    plt.plot(xList, yList, '*-')  # 绘制曲线
    plt.fill_between(xList, yList, color='skyblue', alpha=1)  # 填充曲线下方的颜色
    plt.xlabel(xLabel)  # 设置x轴标签
    for i in range(len(xList)):
        plt.text(xList[i], yList[i], str(yList[i]), ha='center', va='bottom', fontsize=10.5)  # 在数据点上标注数值
    plt.yticks([])  # 隐藏y轴刻度
    plt.gca().invert_yaxis()
    plt.savefig('temperature.png')  # 保存图片
try:
    code = api_num.code
    x_arr = api_num.search_24h_date(code)[0]
    y_arr = api_num.search_24h_date(code)[1]
    showResult(x_arr, y_arr, 'Temperature Variation', 'Time', 'Temperature')  # 调用函数展示结果
except:
    app = QApplication([])
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setText("当前服务不可用\n(没钱购买，每天限量，哭)")
    msg_box.setWindowTitle("警告")
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec_()
    sys.exit()

