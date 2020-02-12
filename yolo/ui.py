# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Second.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import os
import shutil
import time

from PyQt5.QtGui import QPixmap
import ftp_combine01 as cnn

try:
    # new location for sip
    # https://www.riverbankcomputing.com/static/Docs/PyQt5/incompatibilities.html#pyqt-v5-11
    from PyQt5 import sip, Qt
except ImportError:
    import sip

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl, QFileInfo, QDir, QThread, pyqtSignal
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QFileDialog, QMessageBox

# from fbs_runtime.application_context.PyQt5 import ApplicationContext

num = 0
name_in = "test"

class Ui_main():
    global name_in

    def __init__(self):
        self.horizontalLayoutWidget = QtWidgets.QWidget(main)
        self.verticalLayoutWidget = QtWidgets.QWidget(main)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(main)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(main)
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.submitButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.counting = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.movementheatmap = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.movementline = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.heatmap = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.selectButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.menuLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.title = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.titleLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.showWidget = QVideoWidget(main)
        self.peopleLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.peopleNo = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.peopleBox = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget_3)
        self.progressLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.resultWidget = QVideoWidget(main)

    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(1024, 768)
        main.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        main.setAcceptDrops(False)
        main.setAutoFillBackground(False)
        main.setFixedSize(main.size())
        #
        #
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 1021, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.titleLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.titleLayout.setContentsMargins(0, 0, 0, 0)
        self.titleLayout.setSpacing(0)
        self.titleLayout.setObjectName("titleLayout")
        self.title.setEnabled(True)

        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)

        self.title.setFont(font)
        self.title.setTextFormat(QtCore.Qt.AutoText)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.titleLayout.addWidget(self.title)
        #
        #
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(main)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(50, 130, 391, 271))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.menuLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.menuLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.menuLayout.setContentsMargins(0, 0, 0, 0)
        self.menuLayout.setSpacing(0)
        self.menuLayout.setObjectName("menuLayout")

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.menuLayout.addItem(spacerItem)

        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.selectButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectButton.sizePolicy().hasHeightForWidth())
        self.selectButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectButton.setFont(font)
        self.selectButton.setObjectName("selectButton")
        self.selectButton.clicked.connect(self.abrir)
        self.buttonLayout.addWidget(self.selectButton)

        self.submitButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submitButton.sizePolicy().hasHeightForWidth())
        self.submitButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        self.buttonLayout.addWidget(self.submitButton)
        self.submitButton.clicked.connect(self.run_process)
        self.menuLayout.addLayout(self.buttonLayout)


        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.menuLayout.addItem(spacerItem1)

        self.checkBoxLayout = QtWidgets.QHBoxLayout()
        self.checkBoxLayout.setObjectName("checkBoxLayout")

        self.heatmap = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heatmap.sizePolicy().hasHeightForWidth())
        self.heatmap.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.heatmap.setFont(font)
        self.heatmap.setObjectName("heatmap")
        self.checkBoxLayout.addWidget(self.heatmap, 0, QtCore.Qt.AlignHCenter)

        self.counting = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.counting.sizePolicy().hasHeightForWidth())
        self.counting.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.counting.setFont(font)
        self.counting.setObjectName("counting")
        self.checkBoxLayout.addWidget(self.counting)
        self.menuLayout.addLayout(self.checkBoxLayout)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.menuLayout.addItem(spacerItem2)
        #
        #
        self.showWidget.setGeometry(QtCore.QRect(500, 130, 480, 270))
        self.showWidget.setObjectName("showWidget")
        #
        #
        self.label = QtWidgets.QLabel(main)
        self.label.setGeometry(QtCore.QRect(496, 450, 481, 271))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("pixLabel")
        #
        #
        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)
        #
        #
        self.mediaPlayer.setVideoOutput(self.showWidget)
        #
        #
        # self.horizontalLayoutWidget.setGeometry(QtCore.QRect(670, 400, 171, 51))
        # self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        # self.peopleBox.setContentsMargins(0, 0, 0, 0)
        # self.peopleBox.setObjectName("peopleBox")
        # self.peopleNo.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.peopleNo.setSmallDecimalPoint(False)
        # self.peopleNo.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        # self.peopleNo.setObjectName("peopleNo")
        # self.peopleBox.addWidget(self.peopleNo)
        # font = QtGui.QFont()
        # font.setPointSize(11)
        # self.peopleLabel.setFont(font)
        # self.peopleLabel.setAlignment(QtCore.Qt.AlignCenter)
        # self.peopleLabel.setObjectName("peopleLabel")
        # self.peopleBox.addWidget(self.peopleLabel)
        #
        #
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(50, 450, 421, 271))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")

        self.progressLayout.setContentsMargins(0, 0, 0, 0)
        self.progressLayout.setObjectName("progressLayout")

        self.progressBar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setTextVisible(False)
        self.progressLayout.addWidget(self.progressBar)
        #
        #

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "[FTP] CCC System Beta"))
        self.title.setText(_translate("main", "[FTP] CCC System Beta"))
        self.selectButton.setText(_translate("main", "Select Video"))
        self.heatmap.setText(_translate("main", "Heatmap"))
        self.counting.setText(_translate("main", "Counting people"))
        self.submitButton.setText(_translate("main", "Submit"))
        self.peopleLabel.setText(_translate("main", "People"))
        self.label.setText(_translate("main", "Not Available"))

    def abrir(self):
        global name_in
        selected_file, _ = QFileDialog.getOpenFileName(None, "Select a video", ".",
                                                  "Video Files (*.mp4 *.flv *.ts *.mts *.avi)")
        if selected_file != '':
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(selected_file)))
            self.play()
            name_of_file = QFileInfo(selected_file).fileName()
            name_in = str(name_of_file)

            if QFileInfo(selected_file).path() != QDir.currentPath():
                shutil.copy(selected_file, os.getcwd()+"\\"+name_of_file)

        self.progressBar.setValue(0)

    def play(self):
        self.mediaPlayer.play()

    def run_process(self):
        if "test" in name_in:
            return
        else:
            self.progressBar.setValue(10)
            command = "conda activate yolov3 && python ftp_combine01.py --video "+name_in
            self.progressBar.setValue(30)
            os.system(command)
            self.progressBar.setValue(60)
            self.show_video()
            self.progressBar.setValue(80)
            if self.heatmap.isChecked():
                self.show_heatmap()
            if self.counting.isChecked():
                self.show_counting()
            self.progressBar.setValue(100)

    def show_video(self):
        directory = QDir(os.getcwd())
        directory.setFilter(QDir.Files | QDir.NoDotDot | QDir.NoDotAndDotDot)
        directory.setSorting(QDir.Time)
        set_filter = ["*.avi"]
        directory.setNameFilters(set_filter)

        for show in directory.entryInfoList():
            print("%s %s" % (show.size(), show.fileName()))
            out = show.fileName()
            break

        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile(os.getcwd()+"\\"+out)))
        self.play()

    def show_heatmap(self):
        directory = QDir(os.getcwd())
        directory.setFilter(QDir.Files | QDir.NoDotDot | QDir.NoDotAndDotDot)
        directory.setSorting(QDir.Time)
        set_filter = ["*.jpg"]
        directory.setNameFilters(set_filter)

        for show in directory.entryInfoList():
            print("%s %s" % (show.size(), show.fileName()))
            if "heatmap" in show.fileName():
                out = show.fileName()
                break

        w = self.label.width()
        h = self.label.height()

        pixmap = QPixmap(out)
        pixmap = pixmap.scaled(w, h, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)

    def show_counting(self):
        directory = QDir(os.getcwd())
        directory.setFilter(QDir.Files | QDir.NoDotDot | QDir.NoDotAndDotDot)
        directory.setSorting(QDir.Time)
        set_filter = ["*.jpg"]
        directory.setNameFilters(set_filter)

        for show in directory.entryInfoList():
            print("%s %s" % (show.size(), show.fileName()))
            if "graph" in show.fileName():
                out = show.fileName()
                break

        w = self.label.width()
        h = self.label.height()

        pixmap = QPixmap(out)
        pixmap = pixmap.scaled(w, h, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)

    def set_progressbar(self):
        maxval = 80
        start = 0
        print(1)
        while start <= maxval:
            start = start + 3
            self.progressBar.setValue(start)
            time.sleep(1)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QDialog()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())

