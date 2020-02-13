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
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(main)
        self.statusTitle = QtWidgets.QLabel(main)
        self.countingLabel = QtWidgets.QLabel(main)
        self.statusLabel = QtWidgets.QLabel(main)
        self.heatmapLabel = QtWidgets.QLabel(main)
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget(main)
        self.counting = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.heatmap = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.selectButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.buttonLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)

    def setupUi(self, main):
        main.setObjectName("main")
        main.setWindowModality(QtCore.Qt.NonModal)
        main.resize(1230, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main.sizePolicy().hasHeightForWidth())
        main.setSizePolicy(sizePolicy)
        main.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        main.setAcceptDrops(False)
        main.setAutoFillBackground(False)
        main.setModal(False)
        #
        #
        # self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 1021, 80))
        # self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        #
        # self.titleLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        # self.titleLayout.setContentsMargins(0, 0, 0, 0)
        # self.titleLayout.setSpacing(0)
        # self.titleLayout.setObjectName("titleLayout")
        # self.title.setEnabled(True)
        #
        # font = QtGui.QFont()
        # font.setPointSize(26)
        # font.setBold(True)
        # font.setWeight(75)
        #
        # self.title.setFont(font)
        # self.title.setTextFormat(QtCore.Qt.AutoText)
        # self.title.setAlignment(QtCore.Qt.AlignCenter)
        # self.title.setObjectName("title")
        # self.titleLayout.addWidget(self.title)
        #
        #
        # self.verticalLayoutWidget_2 = QtWidgets.QWidget(main)
        # self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(50, 130, 391, 271))
        # self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        # self.menuLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        # self.menuLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        # self.menuLayout.setContentsMargins(0, 0, 0, 0)
        # self.menuLayout.setSpacing(0)
        # self.menuLayout.setObjectName("menuLayout")
        #
        # spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # self.menuLayout.addItem(spacerItem)
        #
        # self.buttonLayout = QtWidgets.QHBoxLayout()
        # self.buttonLayout.setObjectName("buttonLayout")
        # self.selectButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.selectButton.sizePolicy().hasHeightForWidth())
        # self.selectButton.setSizePolicy(sizePolicy)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.selectButton.setFont(font)
        # self.selectButton.setObjectName("selectButton")
        # self.selectButton.clicked.connect(self.abrir)
        # self.buttonLayout.addWidget(self.selectButton)
        #
        # self.submitButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.submitButton.sizePolicy().hasHeightForWidth())
        # self.submitButton.setSizePolicy(sizePolicy)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.submitButton.setFont(font)
        # self.submitButton.setObjectName("submitButton")
        # self.buttonLayout.addWidget(self.submitButton)
        # self.submitButton.clicked.connect(self.run_process)
        # self.menuLayout.addLayout(self.buttonLayout)
        #
        # spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        # self.menuLayout.addItem(spacerItem1)
        #
        # self.checkBoxLayout = QtWidgets.QHBoxLayout()
        # self.checkBoxLayout.setObjectName("checkBoxLayout")
        #
        # self.heatmap = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.heatmap.sizePolicy().hasHeightForWidth())
        # self.heatmap.setSizePolicy(sizePolicy)
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.heatmap.setFont(font)
        # self.heatmap.setObjectName("heatmap")
        # self.checkBoxLayout.addWidget(self.heatmap, 0, QtCore.Qt.AlignHCenter)
        #
        # self.counting = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.counting.sizePolicy().hasHeightForWidth())
        # self.counting.setSizePolicy(sizePolicy)
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.counting.setFont(font)
        # self.counting.setObjectName("counting")
        # self.checkBoxLayout.addWidget(self.counting)
        # self.menuLayout.addLayout(self.checkBoxLayout)
        #
        # spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # self.menuLayout.addItem(spacerItem2)
        #
        #
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 420, 1191, 39))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.setObjectName("buttonLayout")

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

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heatmap.sizePolicy().hasHeightForWidth())
        self.heatmap.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.heatmap.setFont(font)
        self.heatmap.setObjectName("heatmap")
        self.buttonLayout.addWidget(self.heatmap)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.counting.sizePolicy().hasHeightForWidth())
        self.counting.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.counting.setFont(font)
        self.counting.setObjectName("counting")
        self.buttonLayout.addWidget(self.counting)

        spacerItem = QtWidgets.QSpacerItem(600, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem)

        self.submitButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submitButton.sizePolicy().hasHeightForWidth())
        self.submitButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        self.submitButton.clicked.connect(self.run_process)
        self.submitButton.setEnabled(False)
        self.buttonLayout.addWidget(self.submitButton)
        #
        #
        self.videoWidget.setGeometry(QtCore.QRect(20, 20, 380, 380))
        self.videoWidget.setAutoFillBackground(False)
        self.videoWidget.setObjectName("videoWidget")
        #
        #
        self.heatmapLabel.setGeometry(QtCore.QRect(420, 20, 380, 380))
        self.heatmapLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.heatmapLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.heatmapLabel.setObjectName("heatmapLabel")

        self.statusLabel.setGeometry(QtCore.QRect(1140, 460, 70, 30))
        self.statusLabel.setScaledContents(False)
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setIndent(-1)
        self.statusLabel.setObjectName("statusLabel")

        self.countingLabel.setGeometry(QtCore.QRect(830, 20, 380, 380))
        self.countingLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.countingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.countingLabel.setObjectName("countingLabel")
        #
        #
        self.statusTitle.setGeometry(QtCore.QRect(1090, 460, 60, 30))
        self.statusTitle.setScaledContents(False)
        self.statusTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.statusTitle.setIndent(-1)
        self.statusTitle.setObjectName("statusTitle")
        #
        #
        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)
        #
        #
        self.mediaPlayer.setVideoOutput(self.videoWidget)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "[FTP] Triple C System"))
        self.selectButton.setText(_translate("main", "Select Video"))
        self.heatmap.setText(_translate("main", "Heatmap"))
        self.counting.setText(_translate("main", "Counting people"))
        self.submitButton.setText(_translate("main", "Submit"))
        self.heatmapLabel.setText(_translate("main", "Heatmap"))
        self.statusLabel.setText(_translate("main", "Not Ready"))
        self.countingLabel.setText(_translate("main", "Counting People"))
        self.statusTitle.setText(_translate("main", "Status:"))

    def abrir(self):
        global name_in
        selected_file, _ = QFileDialog.getOpenFileName(None, "Select a video", ".",
                                                  "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.mpg)")
        if selected_file != '':
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(selected_file)))
            self.play()
            name_of_file = QFileInfo(selected_file).fileName()
            name_in = str(name_of_file)

            if QFileInfo(selected_file).path() != QDir.currentPath():
                shutil.copy(selected_file, os.getcwd()+"\\"+name_of_file)

            self.statusLabel.setText("Ready")

            self.submitButton.setEnabled(True)

            self.heatmapLabel.clear()
            self.heatmapLabel.setText("Heatmap")

            self.countingLabel.clear()
            self.countingLabel.setText("Counting people")

    def play(self):
        self.mediaPlayer.play()

    def run_process(self):
        self.statusLabel.setText("Processing")
        if "test" in name_in:
            return
        else:
            command = "conda activate yolov3 && python ftp_combine01.py --video "+name_in
            os.system(command)
            self.show_video()
            if self.heatmap.isChecked():
                self.show_heatmap()
            if self.counting.isChecked():
                self.show_counting()
            self.statusLabel.setText("Complete")
            self.selectButton.setEnabled(True)
            self.submitButton.setEnabled(False)

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
        # self.mediaPlayer.setPlaybackRate()
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

        w = self.heatmapLabel.width()
        h = self.heatmapLabel.height()

        pixmap = QPixmap(out)
        pixmap = pixmap.scaled(w, h, QtCore.Qt.KeepAspectRatio)
        self.heatmapLabel.setPixmap(pixmap)

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

        w = self.countingLabel.width()
        h = self.countingLabel.height()

        pixmap = QPixmap(out)
        pixmap = pixmap.scaled(w, h, QtCore.Qt.KeepAspectRatio)
        self.countingLabel.setPixmap(pixmap)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QDialog()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())

