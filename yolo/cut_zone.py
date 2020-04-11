import os
import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PIL import Image

class Menu(QMainWindow):
    global checked
    checked = True

    def __init__(self):
        super().__init__()
        self.drawing = False
        self.startPoint = QPoint()
        self.lastPoint = QPoint()
        self.image = QPixmap("selected_zone.jpg")
        self.setGeometry(100, 100, 500, 300)
        self.resize(self.image.width(), self.image.height())
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)

    def mousePressEvent(self, event):
        self.image = QPixmap("selected_zone.jpg")
        # painter = QPainter(self.image)
        # painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
        if event.button() == Qt.LeftButton:
            # self.image = QPixmap("dog.jpg")
            self.drawing = True
            if checked:
                self.startPoint = event.pos()
            self.lastPoint = event.pos()
            # painter.drawRect(self.startPoint.x(), self.startPoint.y(), (self.lastPoint.x() - self.startPoint.x()),
            #                  (self.lastPoint.y() - self.startPoint.y()))
            # self.update()
            print(self.lastPoint)

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton and self.drawing:
            # painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            # painter.setPen(QPen(Qt.blue, 3, Qt.SolidLine))

    def showdialog(self):
        # msg = QMessageBox()
        # msg.setIcon(QMessageBox.Information)
        #
        # msg.setText("Are you sure?")
        # msg.setWindowTitle("Confirmation")
        # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        #
        # if msg.exec_() == QMessageBox.Cancel:
        #     self.image = QPixmap("selected_zone.jpg")
        #     self.update()

        buttonReply = QMessageBox.question(self, 'Zone is selected!', "Do you want to choose this zone?",
                                           QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        print(int(buttonReply))
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')

            self.crop_image()

            f = open("zone_position.txt", "w+")
            # output = self.startPoint.x() + "," + self.startPoint.y()
            # output.append(self.lastPoint.x() + "," + self.lastPoint.y())
            x1 = self.startPoint.x()
            y1 = self.startPoint.y()
            x2 = self.lastPoint.x()
            y2 = self.lastPoint.y()
            f.write("%d,%d\r\n%d,%d" %(x1,y1,x2,y2))

            self.close()

        if buttonReply == QMessageBox.Cancel:
            print('Cancel')
            self.close()
            command = "python cut_zone.py"
            os.system(command)

    def mouseReleaseEvent(self, event):
        painter = QPainter(self.image)
        painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
        painter.drawRect(self.startPoint.x(), self.startPoint.y(), (self.lastPoint.x() - self.startPoint.x()),
                         (self.lastPoint.y() - self.startPoint.y()))
        self.update()
        if event.button == Qt.LeftButton:
            self.drawing = False

        self.showdialog()

    def crop_image(self):
        imageObject = Image.open("selected_zone.jpg")
        cropped = imageObject.crop((self.startPoint.x(), self.startPoint.y(), self.lastPoint.x(), self.lastPoint.y()))
        cropped.save("cropped_zone.jpg")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainMenu = Menu()
    sys.exit(app.exec_())
