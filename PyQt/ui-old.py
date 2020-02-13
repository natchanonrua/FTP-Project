# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'First.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir, Qt, QUrl, QSize
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar)

class Ui_Dialog(object):
    def setupUi(self, Dialog):

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()

        Dialog.setObjectName("Dialog")
        Dialog.resize(762, 559)
        Dialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Dialog.setAcceptDrops(False)
        Dialog.setAutoFillBackground(False)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(280, 120, 471, 241))
        self.graphicsView.setObjectName("graphicsView")
        # self.graphicsView.addWidget(videoWidget)

        self.movementline = QtWidgets.QCheckBox(Dialog)
        self.movementline.setGeometry(QtCore.QRect(40, 200, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.movementline.setFont(font)
        self.movementline.setObjectName("movementline")
        self.heatmap = QtWidgets.QCheckBox(Dialog)
        self.heatmap.setGeometry(QtCore.QRect(40, 160, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.heatmap.setFont(font)
        self.heatmap.setObjectName("heatmap")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 120, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.abrir)

        self.movementheatmap = QtWidgets.QCheckBox(Dialog)
        self.movementheatmap.setGeometry(QtCore.QRect(40, 240, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.movementheatmap.setFont(font)
        self.movementheatmap.setObjectName("movementheatmap")
        self.counting = QtWidgets.QCheckBox(Dialog)
        self.counting.setGeometry(QtCore.QRect(40, 280, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.counting.setFont(font)
        self.counting.setObjectName("counting")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(500, 380, 251, 161))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 330, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 30, 511, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        #self.pushButton_2.clicked.connect(self.selectFile(self))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.mediaPlayer.setVideoOutput(videoWidget)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.movementline.setText(_translate("Dialog", "Movement line"))
        self.heatmap.setText(_translate("Dialog", "Heatmap"))
        self.movementheatmap.setText(_translate("Dialog", "Movement heatmap"))
        self.counting.setText(_translate("Dialog", "Counting people"))
        self.pushButton.setText(_translate("Dialog", "Select Video"))
        self.pushButton_2.setText(_translate("Dialog", "Submit"))
        self.label.setText(_translate("Dialog", "[FTP] CCC System Beta"))

    def abrir(self):
        fileName, _ = QFileDialog.getOpenFileName(None, "Select a video", ".",
                                                  "Video Files (*.mp4 *.flv *.ts *.mts *.avi)")

        if fileName != '':
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(fileName)))
            self.pushButton.setEnabled(True)
            self.statusBar.showMessage(fileName)
            self.play()

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()


    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
            self.positionSlider.setValue(position)

    def durationChanged(self, duration):
            self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
            self.mediaPlayer.setPosition(position)

    def handleError(self):
            self.playButton.setEnabled(False)
            self.statusBar.showMessage("Error: " + self.mediaPlayer.errorString())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())