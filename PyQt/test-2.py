from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # event actions
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        lay = QtWidgets.QVBoxLayout(central_widget)

        flay = QtWidgets.QFormLayout()

        self.input_le = QtWidgets.QLineEdit()
        input_btn = QtWidgets.QPushButton("Select Input")
        input_btn.clicked.connect(self.select_input)

        self.output_le = QtWidgets.QLineEdit()
        output_btn = QtWidgets.QPushButton("Select Output")
        output_btn.clicked.connect(self.select_output)

        process_btn = QtWidgets.QPushButton("process")
        process_btn.clicked.connect(self.process)

        flay.addRow(self.input_le, input_btn)
        flay.addRow(self.output_le, output_btn)

        lay.addLayout(flay)
        lay.addWidget(process_btn)
        lay.addStretch()

    def select_input(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 
            "Open File", 
            QtCore.QDir.homePath(),
            "Images (*.png *.xpm *.jpg)") 
        self.input_le.setText(fileName)

    def select_output(self):
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, 
            "Open File", 
            QtCore.QDir.homePath(),
            "Images (*.png *.xpm *.jpg)") 
        self.output_le.setText(fileName)

    def process(self):
        if  self.input_le.text() and self.output_le.text():
            QtCore.QProcess.startDetached(r"C:\Users\IEUser\Desktop\convertstuff.exe", 
                ["-i", self.input_le.text(), "-o", self.output_le.text()])
        else:
            print("empty arguments"





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_()) 