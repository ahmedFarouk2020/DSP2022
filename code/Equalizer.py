# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EqualizersEIbux.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Source_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1080, 850)
        font = QFont()
        font.setFamily(u"Arial Unicode MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setTabletTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.OriginalSignalGroupbox = QGroupBox(self.centralwidget)
        self.OriginalSignalGroupbox.setObjectName(u"OriginalSignalGroupbox")
        font1 = QFont()
        font1.setFamily(u"Arial Unicode MS")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.OriginalSignalGroupbox.setFont(font1)
        self.gridLayout_4 = QGridLayout(self.OriginalSignalGroupbox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.OriginalSignalViewer = QGraphicsView(self.OriginalSignalGroupbox)
        self.OriginalSignalViewer.setObjectName(u"OriginalSignalViewer")
        self.OriginalSignalViewer.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.OriginalSignalViewer.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.gridLayout_4.addWidget(self.OriginalSignalViewer, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.OriginalSignalGroupbox, 0, 0, 1, 1)

        self.SpectrogramGroupBox = QGroupBox(self.centralwidget)
        self.SpectrogramGroupBox.setObjectName(u"SpectrogramGroupBox")
        self.SpectrogramGroupBox.setFont(font1)
        self.SpectrogramGroupBox.setStyleSheet(u"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.verticalLayout = QVBoxLayout(self.SpectrogramGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SignalBeforeEditiing_2 = QGraphicsView(self.SpectrogramGroupBox)
        self.SignalBeforeEditiing_2.setObjectName(u"SignalBeforeEditiing_2")
        self.SignalBeforeEditiing_2.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.SignalBeforeEditiing_2.setStyleSheet(u"background-color:rgb(0,0,0)")

        self.verticalLayout.addWidget(self.SignalBeforeEditiing_2)


        self.gridLayout.addWidget(self.SpectrogramGroupBox, 0, 1, 3, 1)

        self.EditedSignalGroupBox = QGroupBox(self.centralwidget)
        self.EditedSignalGroupBox.setObjectName(u"EditedSignalGroupBox")
        self.EditedSignalGroupBox.setFont(font1)
        self.gridLayout_5 = QGridLayout(self.EditedSignalGroupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.EditedSignalViewer = QGraphicsView(self.EditedSignalGroupBox)
        self.EditedSignalViewer.setObjectName(u"EditedSignalViewer")
        self.EditedSignalViewer.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.EditedSignalViewer.setStyleSheet(u"background-color:rgb(0,0,0)")

        self.gridLayout_5.addWidget(self.EditedSignalViewer, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.EditedSignalGroupBox, 2, 0, 1, 1)

        self.SignalEditorGroupBox = QGroupBox(self.centralwidget)
        self.SignalEditorGroupBox.setObjectName(u"SignalEditorGroupBox")
        self.SignalEditorGroupBox.setFont(font1)
        self.gridLayout_3 = QGridLayout(self.SignalEditorGroupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Slider1 = QSlider(self.SignalEditorGroupBox)
        self.Slider1.setObjectName(u"Slider1")
        self.Slider1.setCursor(QCursor(Qt.ClosedHandCursor))
        self.Slider1.setMinimum(1)
        self.Slider1.setMaximum(10)
        self.Slider1.setOrientation(Qt.Vertical)
        self.Slider1.setTickPosition(QSlider.TicksAbove)
        self.Slider1.setTickInterval(1)

        self.gridLayout_3.addWidget(self.Slider1, 0, 2, 1, 1)

        self.Slider3 = QSlider(self.SignalEditorGroupBox)
        self.Slider3.setObjectName(u"Slider3")
        self.Slider3.setCursor(QCursor(Qt.ClosedHandCursor))
        self.Slider3.setMinimum(1)
        self.Slider3.setMaximum(10)
        self.Slider3.setPageStep(10)
        self.Slider3.setOrientation(Qt.Vertical)
        self.Slider3.setTickPosition(QSlider.TicksAbove)
        self.Slider3.setTickInterval(1)

        self.gridLayout_3.addWidget(self.Slider3, 0, 1, 1, 1)

        self.Slider2 = QSlider(self.SignalEditorGroupBox)
        self.Slider2.setObjectName(u"Slider2")
        self.Slider2.setCursor(QCursor(Qt.ClosedHandCursor))
        self.Slider2.setMinimum(1)
        self.Slider2.setMaximum(10)
        self.Slider2.setOrientation(Qt.Vertical)
        self.Slider2.setInvertedAppearance(False)
        self.Slider2.setTickPosition(QSlider.TicksAbove)
        self.Slider2.setTickInterval(1)

        self.gridLayout_3.addWidget(self.Slider2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.SignalEditorGroupBox, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1080, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Equalizer", None))
        self.OriginalSignalGroupbox.setTitle(QCoreApplication.translate("MainWindow", u"Signal Before Editing", None))
        self.SpectrogramGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Spectrogram", None))
        self.EditedSignalGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Signal After Editing", None))
        self.SignalEditorGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Signal Editor", None))
#if QT_CONFIG(tooltip)
        self.Slider2.setToolTip("")
#endif // QT_CONFIG(tooltip)
    # retranslateUi

