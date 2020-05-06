# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Second.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
# import os
import calendar
import shutil
import time

from PIL import Image
from PyQt5.QtGui import QPixmap, QPainter, QPen

# import ftp_combine01 as cnn
from moviepy.video.fx.crop import crop

try:
    # new location for sip
    # https://www.riverbankcomputing.com/static/Docs/PyQt5/incompatibilities.html#pyqt-v5-11
    from PyQt5 import sip, Qt
except ImportError:
    import sip

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl, QFileInfo, QDir, QThread, pyqtSignal, QSize, QPoint, QRect
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QMainWindow, QApplication

from moviepy.editor import *

# from fbs_runtime.application_context.PyQt5 import ApplicationContext

num = 0
name_in = "test"


def get_zone_position():
    m = open('zone_position.txt', 'r').read()
    lines = m.split('\n')
    x = []
    y = []
    for line in lines:
        if len(line) > 1:
            x0, y0 = line.split(',')
            x.append(x0)
            y.append(y0)
    x1 = int(x[0])
    x2 = int(x[1])
    y1 = int(y[0])
    y2 = int(y[1])

    return x1, y1, x2, y2


class Ui_main():
    global name_in, out, selected, checked, zone_cutted
    checked = True


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
        self.zone_cutted = False

    def setupUi(self, main):
        main.setObjectName("main")
        main.setWindowModality(QtCore.Qt.NonModal)
        main.resize(1230, 830)
        main.setFixedSize(QSize(1230, 830))
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
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 420, 1191, 39))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.setObjectName("buttonLayout")

        self.heatmapLabel.setGeometry(QtCore.QRect(420, 20, 380, 380))
        self.heatmapLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.heatmapLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.heatmapLabel.setObjectName("heatmapLabel")

        self.countingLabel.setGeometry(QtCore.QRect(830, 20, 380, 380))
        self.countingLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.countingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.countingLabel.setObjectName("countingLabel")

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

        spacerItem = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem)

        self.beginTimeLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.beginTimeLabel.setFont(font)
        self.beginTimeLabel.setObjectName("beginTimeLabel")
        self.buttonLayout.addWidget(self.beginTimeLabel)

        self.beginTimeEdit = QtWidgets.QTimeEdit(self.horizontalLayoutWidget_3)
        self.beginTimeEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.beginTimeEdit.setObjectName("beginTimeEdit")
        self.buttonLayout.addWidget(self.beginTimeEdit)

        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem1)

        self.startTimeLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.startTimeLabel.setFont(font)
        self.startTimeLabel.setObjectName("startTimeLabel")
        self.buttonLayout.addWidget(self.startTimeLabel)

        self.startTimeEdit = QtWidgets.QTimeEdit(self.horizontalLayoutWidget_3)
        self.startTimeEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.startTimeEdit.setObjectName("startTimeEdit")
        self.buttonLayout.addWidget(self.startTimeEdit)

        self.endTimeLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.endTimeLabel.setFont(font)
        self.endTimeLabel.setObjectName("endTimeLabel")
        self.buttonLayout.addWidget(self.endTimeLabel)

        self.endTimeEdit = QtWidgets.QTimeEdit(self.horizontalLayoutWidget_3)
        self.endTimeEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.endTimeEdit.setObjectName("endTimeEdit")
        self.buttonLayout.addWidget(self.endTimeEdit)

        # self.submitButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.submitButton = QtWidgets.QPushButton(main)
        self.submitButton.setGeometry(QtCore.QRect(940, 540, 266, 41))

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
        # self.buttonLayout.addWidget(self.submitButton)
        #
        #
        self.videoWidget.setGeometry(QtCore.QRect(20, 20, 380, 380))
        self.videoWidget.setAutoFillBackground(False)
        self.videoWidget.setObjectName("videoWidget")
        #
        #
        self.statusLabel.setGeometry(QtCore.QRect(1140, 580, 71, 31))
        self.statusLabel.setScaledContents(False)
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setIndent(-1)
        self.statusLabel.setObjectName("statusLabel")

        self.statusTitle.setGeometry(QtCore.QRect(1090, 580, 61, 31))
        self.statusTitle.setScaledContents(False)
        self.statusTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.statusTitle.setIndent(-1)
        self.statusTitle.setObjectName("statusTitle")
        #
        # ZONE NEW
        self.zoneButton = QtWidgets.QPushButton(main)
        self.zoneButton.setGeometry(QtCore.QRect(110, 770, 291, 37))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoneButton.sizePolicy().hasHeightForWidth())
        self.zoneButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.zoneButton.setFont(font)
        self.zoneButton.setObjectName("zoneButton")
        self.zoneButton.clicked.connect(self.select_zone)
        self.zoneButton.setEnabled(False)

        # self.outputdiButton = QtWidgets.QPushButton(main)
        # self.outputdiButton.setGeometry(QtCore.QRect(546, 482, 171, 41))
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.outputdiButton.sizePolicy().hasHeightForWidth())
        # self.outputdiButton.setSizePolicy(sizePolicy)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.outputdiButton.setFont(font)
        # self.outputdiButton.setObjectName("outputdiButton")
        # self.outputdiText = QtWidgets.QTextEdit(main)
        # self.outputdiText.setGeometry(QtCore.QRect(730, 490, 481, 31))
        # self.outputdiText.setObjectName("outputdiText")
        self.zoneLabel = QtWidgets.QLabel(main)
        self.zoneLabel.setGeometry(QtCore.QRect(20, 483, 480, 270))
        self.zoneLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.zoneLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.zoneLabel.setObjectName("zoneLabel")
        #
        #
        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)
        #
        #
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        #
        #
        # self.setGeometry(100, 100, 500, 300)
        # self.resize(self.image.width(), self.image.height())
        # self.show()
        #
        #
        self.lastPoint = QPoint()
        self.startPoint = QPoint()
        self.drawing = False

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "[FTP] Triple C System"))
        self.selectButton.setText(_translate("main", "Select Video"))
        self.heatmap.setText(_translate("main", "Heatmap"))
        self.counting.setText(_translate("main", "Counting People"))
        self.submitButton.setText(_translate("main", "Submit"))
        self.heatmapLabel.setText(_translate("main", "Heatmap"))
        self.statusLabel.setText(_translate("main", "Not Ready"))
        self.countingLabel.setText(_translate("main", "Counting People"))
        self.statusTitle.setText(_translate("main", "Status:"))
        self.beginTimeLabel.setText(_translate("main", "Begin Time:"))
        self.startTimeLabel.setText(_translate("main", "Start at:"))
        self.endTimeLabel.setText(_translate("main", "End at:"))
        self.beginTimeEdit.setDisplayFormat(_translate("main", "HH:mm:ss"))
        self.startTimeEdit.setDisplayFormat(_translate("main", "HH:mm:ss"))
        self.endTimeEdit.setDisplayFormat(_translate("main", "HH:mm:ss"))

        self.zoneButton.setText(_translate("main", "Zone Separate Analysis"))
        # self.outputdiButton.setText(_translate("main", "Output Directory"))
        self.zoneLabel.setText(_translate("main", "Zone Separate Analysis"))

    def abrir(self):
        global name_in
        selected_file, _ = QFileDialog.getOpenFileName(None, "Select a video", ".",
                                                       "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.mpg)")
        if selected_file != '':
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(selected_file)))
            self.play()
            name_of_file = QFileInfo(selected_file).fileName()
            self.selected = name_of_file
            self.name_in = name_of_file
            if QFileInfo(selected_file).path() != QDir.currentPath():
                shutil.copy(selected_file, os.getcwd() + "\\" + name_of_file)

            f = open("zone_position.txt", "w+")

            self.statusLabel.setText("Ready")
            self.submitButton.setEnabled(True)
            self.zoneButton.setEnabled(True)
            self.heatmapLabel.clear()
            self.heatmapLabel.setText("Heatmap")

            self.countingLabel.clear()
            self.countingLabel.setText("Counting people")

            clip = VideoFileClip(name_of_file)
            clip.save_frame("selected_zone.jpg", 1)

            w = self.zoneLabel.width()
            h = self.zoneLabel.height()

            pixmap = QPixmap("selected_zone.jpg")
            pixmap = pixmap.scaled(w, h, QtCore.Qt.KeepAspectRatio)

            self.zoneLabel.setPixmap(pixmap)

            # self.select_zone()

    def play(self):
        self.mediaPlayer.play()

    def run_process(self):
        if (self.beginTimeEdit.time().toString() > self.startTimeEdit.time().toString()) or (self.beginTimeEdit.time().toString() > self.endTimeEdit.time().toString()):
            self.startTimeEdit.setTime(self.beginTimeEdit.time())
            self.endTimeEdit.setTime(self.beginTimeEdit.time())
            print(1)
            self.statusLabel.setText("Time Error")
        else:
            if self.startTimeEdit.time().toString() > self.endTimeEdit.time().toString():
                self.endTimeEdit.setTime(self.startTimeEdit.time())
                print(2)
                self.statusLabel.setText("Time Error")
            else:
                if (self.beginTimeEdit.time().toString() != self.endTimeEdit.time().toString()) or (self.startTimeEdit.time().toString() != self.endTimeEdit.time().toString()):
                    self.write_time()
                    self.statusLabel.setText("Converting")
                    self.cut_video()
                    self.statusLabel.setText("Processing")

                command = "conda activate yolov3 && python ftp_combine01.py --video " + self.name_in
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
        # print(1)
        if self.zone_cutted:
            # print(2)
            x1, y1, x2, y2 = get_zone_position()

            clip = VideoFileClip(out)
            cut_video = crop(clip, x1, y1, x2, y2)

            name_of_file = QFileInfo(out).baseName() + "_zone.avi"
            cut_video.write_videofile(name_of_file, codec='mpeg4', audio=False)

        else:
            # print(3)
            name_of_file = out
        # print(4)
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile(os.getcwd() + "\\" + name_of_file))
        )
        # print(5)
        # self.mediaPlayer.setPlaybackRate()
        self.play()
        # print(6)

    def show_heatmap(self):
        # print("a")
        directory = QDir(os.getcwd())
        directory.setFilter(QDir.Files | QDir.NoDotDot | QDir.NoDotAndDotDot)
        directory.setSorting(QDir.Time)
        set_filter = ["*.jpg"]
        directory.setNameFilters(set_filter)
        # print("b")
        for show in directory.entryInfoList():
            print("%s %s" % (show.size(), show.fileName()))
            if "heatmap" in show.fileName():
                out = show.fileName()
                break
        # print("c")
        w = self.heatmapLabel.width()
        h = self.heatmapLabel.height()
        # print("d")
        # print("%r", self.zone_cutted)
        if self.zone_cutted:
            x1, y1, x2, y2 = get_zone_position()

            imageObject = Image.open(out)
            cropped = imageObject.crop((x1, y1, x2, y2))
            name_of_file = QFileInfo(out).baseName() + "_zone.jpg"
            cropped.save(name_of_file)

            pixmap = QPixmap(name_of_file)
        else:
            pixmap = QPixmap(out)
        # print("e")
        pixmap = pixmap.scaled(w, h, QtCore.Qt.KeepAspectRatio)
        self.heatmapLabel.setPixmap(pixmap)
        # print("f")

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

    def cut_video(self):
        file = QFileInfo(self.selected).fileName()
        clip = VideoFileClip(file)
        starttime_hour = int(self.startTimeEdit.time().hour()) - int(self.beginTimeEdit.time().hour())
        starttime_minute = int(self.startTimeEdit.time().minute()) - int(self.beginTimeEdit.time().minute())
        starttime_second = int(self.startTimeEdit.time().second()) - int(self.beginTimeEdit.time().second())
        endtime_hour = int(self.endTimeEdit.time().hour()) - int(self.beginTimeEdit.time().hour())
        endtime_minute = int(self.endTimeEdit.time().minute()) - int(self.beginTimeEdit.time().minute())
        endtime_second = int(self.endTimeEdit.time().second()) - int(self.beginTimeEdit.time().second())

        cut_video = clip.subclip((starttime_hour, starttime_minute, starttime_second),
                                 (endtime_hour, endtime_minute, endtime_second))

        # m = open('zone_position.txt', 'r').read()
        # lines = m.split('\n')
        # x = []
        # y = []
        # for line in lines:
        #     if len(line) > 1:
        #         x0, y0 = line.split(',')
        #         x.append(x0)
        #         y.append(y0)
        # x1 = x[0]
        # x2 = x[1]
        # y1 = y[0]
        # y2 = y[1]
        #
        # cut_video = crop(cut_video, x1, y1, x2, y2)

        name_of_file = QFileInfo(self.selected).baseName() + "_cut.avi"
        self.name_in = str(name_of_file)
        cut_video.write_videofile(name_of_file, codec='mpeg4', audio=False)

    def write_time(self):
        h = int(self.startTimeEdit.time().hour())
        m = int(self.startTimeEdit.time().minute())
        s = int(self.startTimeEdit.time().second())
        x = "1970/01/01 " + str(h) + ":" + str(m) + ":" + str(s)
        x1 = str(h) + ":" + str(m) + ":" + str(s)
        fun = time.strptime(x, "%Y/%m/%d %H:%M:%S")
        y = calendar.timegm(fun)
        f = open("soul.txt", "w+")
        f.write("%s,%d\r\n" % (x1, y))

    def select_zone(self):
        file = QFileInfo(self.selected).fileName()
        clip = VideoFileClip(file)
        clip.save_frame("selected_zone.jpg", 1)

        self.zone_cutted = True

        # self.image = QPixmap('cutzone.jpg')
        # self.zone_pic = self.image.scaled(self.image.size(), QtCore.Qt.KeepAspectRatio)
        # self.zoneLabel.setScaledContents(True)
        # self.zoneLabel.setPixmap(self.zone_pic)

        command = "python cut_zone.py"
        os.system(command)

        w = self.zoneLabel.width()
        h = self.zoneLabel.height()

        pixmap = QPixmap("cropped_zone.jpg")
        pixmap = pixmap.scaled(w, h, QtCore.Qt.KeepAspectRatio)

        # time.sleep(5)

        self.zoneLabel.setPixmap(pixmap)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QDialog()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())
