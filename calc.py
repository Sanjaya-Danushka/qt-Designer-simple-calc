from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.pushButton_eqal = None
        self.pushButton_dot = None
        self.pushButton_3 = None
        self.pushButton_plus = None
        self.pushButton_minus = None
        self.pushButton_multiply = None
        self.pushButton_9 = None
        self.pushButton_6 = None
        self.menubar = None
        self.pushButton_0 = None
        self.pushButton_8 = None
        self.pushButton_5 = None
        self.pushButton_2 = None
        self.pushButton_pm = None
        self.pushButton_1 = None
        self.pushButton_4 = None
        self.pushButton_divide = None
        self.pushButton_arrow = None
        self.pushButton_7 = None
        self.pushButton_c = None
        self.Button_percent = None
        self.frame = None
        self.output_label = None
        self.centralwidget = None
        self.statusbar = None

    def setupUi(self, Main_Window):
        Main_Window.setObjectName("MainWindow")
        Main_Window.resize(361, 569)
        self.centralwidget = QtWidgets.QWidget(parent=Main_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.output_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(10, 0, 341, 91))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        self.output_label.setFont(font)
        self.output_label.setStyleSheet(
            "color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, "
            "255, 255, 255));")
        self.output_label.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.output_label.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.output_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.output_label.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.TextEditable | QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.output_label.setObjectName("output_label")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 100, 341, 431))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.Button_percent = QtWidgets.QPushButton(parent=self.frame,
                                                    clicked=lambda: self.press_it("%"))

        self.Button_percent.setGeometry(QtCore.QRect(10, 10, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.Button_percent.setFont(font)
        self.Button_percent.setObjectName("Button_percent")
        self.pushButton_c = QtWidgets.QPushButton(parent=self.frame,
                                                  clicked=lambda: self.press_it("c"))
        self.pushButton_c.setGeometry(QtCore.QRect(90, 10, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.pushButton_c.setFont(font)
        self.pushButton_c.setAutoFillBackground(False)
        self.pushButton_c.setStyleSheet("")
        self.pushButton_c.setObjectName("pushButton_c")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.frame,
                                                  clicked=lambda: self.press_it("7"))
        self.pushButton_7.setGeometry(QtCore.QRect(10, 100, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_arrow = QtWidgets.QPushButton(parent=self.frame,
                                                      clicked=lambda: self.remove_it())
        self.pushButton_arrow.setGeometry(QtCore.QRect(170, 10, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_arrow.setFont(font)
        self.pushButton_arrow.setObjectName("pushButton_arrow")
        self.pushButton_divide = QtWidgets.QPushButton(parent=self.frame,
                                                       clicked=lambda: self.press_it("/"))
        self.pushButton_divide.setGeometry(QtCore.QRect(250, 10, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_divide.setFont(font)
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.frame,
                                                  clicked=lambda: self.press_it("4"))
        self.pushButton_4.setGeometry(QtCore.QRect(10, 180, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_1 = QtWidgets.QPushButton(parent=self.frame,
                                                  clicked=lambda: self.press_it("1"))
        self.pushButton_1.setGeometry(QtCore.QRect(10, 260, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_pm = QtWidgets.QPushButton(parent=self.frame,
                                                   clicked=lambda: self.pm_it())
        self.pushButton_pm.setGeometry(QtCore.QRect(10, 340, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_pm.setFont(font)
        self.pushButton_pm.setObjectName("pushButton_pm")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame,
                                                  clicked=lambda: self.press_it("2"))
        self.pushButton_2.setGeometry(QtCore.QRect(90, 260, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.frame,
                                                  clicked=lambda: self.press_it("5"))
        self.pushButton_5.setGeometry(QtCore.QRect(90, 180, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.frame,
                                                  clicked=lambda: self.press_it("8"))
        self.pushButton_8.setGeometry(QtCore.QRect(90, 100, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_0 = QtWidgets.QPushButton(parent=self.frame,
                                                  clicked=lambda: self.press_it("0"))
        self.pushButton_0.setGeometry(QtCore.QRect(90, 340, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.frame,
                                                  clicked=lambda: self.press_it("6"))
        self.pushButton_6.setGeometry(QtCore.QRect(170, 180, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.frame,
                                                  clicked=lambda: self.press_it("9"))
        self.pushButton_9.setGeometry(QtCore.QRect(170, 100, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_multiply = QtWidgets.QPushButton(parent=self.frame,
                                                         clicked=lambda: self.press_it("*"))
        self.pushButton_multiply.setGeometry(QtCore.QRect(250, 100, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_multiply.setFont(font)
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.pushButton_minus = QtWidgets.QPushButton(parent=self.frame,
                                                      clicked=lambda: self.press_it("-"))
        self.pushButton_minus.setGeometry(QtCore.QRect(250, 180, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_minus.setFont(font)
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_plus = QtWidgets.QPushButton(parent=self.frame,
                                                     clicked=lambda: self.press_it("+"))
        self.pushButton_plus.setGeometry(QtCore.QRect(250, 260, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame,
                                                  clicked=lambda: self.press_it("3"))
        self.pushButton_3.setGeometry(QtCore.QRect(170, 260, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_dot = QtWidgets.QPushButton(parent=self.frame,
                                                    clicked=lambda: self.dot_it())
        self.pushButton_dot.setGeometry(QtCore.QRect(170, 340, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_dot.setFont(font)
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_eqal = QtWidgets.QPushButton(parent=self.frame,
                                                     clicked=lambda: self.math_it())
        self.pushButton_eqal.setGeometry(QtCore.QRect(250, 340, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_eqal.setFont(font)
        self.pushButton_eqal.setObjectName("pushButton_eqal")
        self.frame.raise_()
        self.output_label.raise_()
        Main_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Main_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 22))
        self.menubar.setObjectName("menubar")
        Main_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Main_Window)
        self.statusbar.setObjectName("statusbar")
        Main_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Main_Window)
        QtCore.QMetaObject.connectSlotsByName(Main_Window)

    def retranslateUi(self, Main_Window):
        _translate = QtCore.QCoreApplication.translate
        Main_Window.setWindowTitle(_translate("MainWindow", "calculator"))
        self.output_label.setToolTip(_translate("MainWindow", "<html><head/><body><p>result</p></body></html>"))
        self.output_label.setText(_translate("MainWindow", "0"))
        self.Button_percent.setText(_translate("MainWindow", "%"))
        self.pushButton_c.setText(_translate("MainWindow", "c"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_arrow.setText(_translate("MainWindow", "<<"))
        self.pushButton_divide.setText(_translate("MainWindow", "/"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_pm.setText(_translate("MainWindow", "+/-"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_multiply.setText(_translate("MainWindow", "X"))
        self.pushButton_minus.setText(_translate("MainWindow", "-"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_dot.setText(_translate("MainWindow", "."))
        self.pushButton_eqal.setText(_translate("MainWindow", "="))
        # ---------calc functions--------------------------------

    def press_it(self, pressed):
        if pressed == 'c':
            self.output_label.setText("0")
        else:
            if self.output_label.text() == "0":
                self.output_label.setText("")

            self.output_label.setText(f'{self.output_label.text()}{pressed}')

    def remove_it(self):
        screen = self.output_label.text()
        screen = screen[:-1]
        self.output_label.setText(f'{screen}.')

    def dot_it(self):
        screen = self.output_label.text()
        if screen[-1] == '.':
            pass
        else:
            self.output_label.setText(f'{screen}.')

    def pm_it(self):
        screen = self.output_label.text()
        if screen[0] == '-':
            self.output_label.setText(f'{screen[1:]}')
        else:
            self.output_label.setText(f'-{screen}')

    def math_it(self):
        try:
            self.output_label.setText(str(eval(self.output_label.text())))
        except:
            self.output_label.setText("error")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
