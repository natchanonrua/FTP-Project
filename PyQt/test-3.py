import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap, QPainter, QPen


class Menu(QMainWindow):
    global checked
    checked = True

    def __init__(self):
        super().__init__()
        self.drawing = False
        self.startPoint = QPoint()
        self.lastPoint = QPoint()
        self.image = QPixmap("cutzone.jpg")
        self.setGeometry(100, 100, 500, 300)
        self.resize(self.image.width(), self.image.height())
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)

    def mousePressEvent(self, event):
        self.image = QPixmap("cutzone.jpg")
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



    def mouseReleaseEvent(self, event):
        painter = QPainter(self.image)
        painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
        painter.drawRect(self.startPoint.x(), self.startPoint.y(), (self.lastPoint.x() - self.startPoint.x()),
                         (self.lastPoint.y() - self.startPoint.y()))
        painter.drawRect(656,595,136,392)
        painter.drawRect(627,607,121,79)
        self.update()
        if event.button == Qt.LeftButton:
            self.drawing = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainMenu = Menu()
    sys.exit(app.exec_())
