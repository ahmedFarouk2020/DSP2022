# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Task3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from display_imgAndcomp import DisplayImgComp,PromptError
from Mixer import Mixer
import Components as components
import matplotlib.pyplot as plt
import os


class mixingRationSlider(QtWidgets.QSlider) : 
    def __init__(self) : 
        super().__init__()
        self.mouseReleaseMethod = None
    
    def mouseReleaseEvent(self,ev) :
        self.mouseReleaseMethod(ev)

class newAction(QtWidgets.QAction):
    def __init__(self,parent,iconPath,objectName,keySequance="",method_to_trigger=None):
        super(newAction,self).__init__()
        self.setParent(parent)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(iconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)
        self.setObjectName(objectName)
        shortCut = QtWidgets.QShortcut(QtGui.QKeySequence(keySequance),parent)
        if method_to_trigger != None : 
            shortCut.activated.connect(method_to_trigger)
            self.triggered.connect(method_to_trigger)

class main_window(QtWidgets.QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.resizeMethod = None
    def resizeEvent(self,ev) :
        self.resizeMethod(ev)

class Ui_MainWindow(DisplayImgComp):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        # MainWindow = QtWidgets.QMainWindow()
        MainWindow.setObjectName("MainWindow")
        #resize event 
        MainWindow.resizeMethod = self.resizeWindow
        MainWindow.resize(800, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PNG/editor.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Img1GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        self.Img1GroupBox.setFont(font)
        self.Img1GroupBox.setObjectName("Img1GroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.Img1GroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.Image1ComboBox = QtWidgets.QComboBox(self.Img1GroupBox)
        self.Image1ComboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Image1ComboBox.setObjectName("Image1ComboBox")
        self.Image1ComboBox.addItem("")
        self.Image1ComboBox.addItem("")
        self.Image1ComboBox.addItem("")
        self.Image1ComboBox.addItem("")
        self.gridLayout.addWidget(self.Image1ComboBox, 0, 1, 1, 1)
        self.Image1ViewerA = QtWidgets.QLabel(self.Img1GroupBox)
        self.Image1ViewerA.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Image1ViewerA.setObjectName("Image1ViewerA")
        self.gridLayout.addWidget(self.Image1ViewerA, 1, 0, 1, 1)
        # Display Img 1
        pixmap = QtGui.QPixmap(self.paths[0])
        pixmap = pixmap.scaled(355, 300, QtCore.Qt.KeepAspectRatio)
        self.Image1ViewerA.setPixmap(pixmap)
        #---------------------------------------------------------------
        self.Image1ViewerB = QtWidgets.QLabel(self.Img1GroupBox)
        self.Image1ViewerB.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Image1ViewerB.setObjectName("Image1ViewerB")
        self.gridLayout.addWidget(self.Image1ViewerB, 1, 1, 1, 1)

        ##############################################################
        self.gridLayout_5.addWidget(self.Img1GroupBox, 0, 0, 1, 1)
        self.MixerGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        self.MixerGroupBox.setFont(font)
        self.MixerGroupBox.setObjectName("MixerGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.MixerGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.OutputLabel = QtWidgets.QLabel(self.MixerGroupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.OutputLabel.setFont(font)
        self.OutputLabel.setObjectName("OutputLabel")
        self.gridLayout_2.addWidget(self.OutputLabel, 0, 2, 1, 1)
        self.OutputCombobox = QtWidgets.QComboBox(self.MixerGroupBox)
        self.OutputCombobox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.OutputCombobox.setObjectName("OutputCombobox")
        self.OutputCombobox.addItem("")
        self.OutputCombobox.addItem("")
        self.gridLayout_2.addWidget(self.OutputCombobox, 0, 3, 1, 1)
        self.Component1Label = QtWidgets.QLabel(self.MixerGroupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Component1Label.setFont(font)
        self.Component1Label.setObjectName("Component1Label")
        self.gridLayout_2.addWidget(self.Component1Label, 1, 0, 1, 1)
        self.Component1ComboBox1 = QtWidgets.QComboBox(self.MixerGroupBox)
        self.Component1ComboBox1.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Component1ComboBox1.setObjectName("Component1ComboBox1")
        self.Component1ComboBox1.addItem("")
        self.Component1ComboBox1.addItem("")
        self.gridLayout_2.addWidget(self.Component1ComboBox1, 1, 1, 1, 1)
        #################################
        self.Component1Slider = mixingRationSlider()
        self.Component1Slider.setParent(self.MixerGroupBox)
        self.Component1Slider.setCursor(
            QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Component1Slider.setMinimum(0)
        self.Component1Slider.setMaximum(100)
        self.Component1Slider.setSingleStep(10)
        self.Component1Slider.setProperty("value", 0)
        self.Component1Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Component1Slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Component1Slider.setObjectName("Component1Slider")
        self.gridLayout_2.addWidget(self.Component1Slider, 1, 2, 1, 3)
        self.Component1SliderStart = QtWidgets.QLabel(self.MixerGroupBox)
        self.Component1SliderStart.setObjectName("Component1SliderStart")
        self.gridLayout_2.addWidget(self.Component1SliderStart, 2, 2, 1, 1)
        self.Component1SliderEnd = QtWidgets.QLabel(self.MixerGroupBox)
        self.Component1SliderEnd.setAlignment(QtCore.Qt.AlignRight
                                              | QtCore.Qt.AlignTrailing
                                              | QtCore.Qt.AlignVCenter)
        self.Component1SliderEnd.setObjectName("Component1SliderEnd")
        self.gridLayout_2.addWidget(self.Component1SliderEnd, 2, 4, 1, 1)
        #################################
        self.Component1ComboBox2 = QtWidgets.QComboBox(self.MixerGroupBox)
        self.Component1ComboBox2.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Component1ComboBox2.setObjectName("Component1ComboBox2")
        self.Component1ComboBox2.addItem("")
        self.Component1ComboBox2.addItem("")
        self.Component1ComboBox2.addItem("")
        self.Component1ComboBox2.addItem("")
        self.Component1ComboBox2.addItem("")
        self.Component1ComboBox2.addItem("")
        self.gridLayout_2.addWidget(self.Component1ComboBox2, 2, 1, 1, 3)
        self.Component2Label = QtWidgets.QLabel(self.MixerGroupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Component2Label.setFont(font)
        self.Component2Label.setObjectName("Component2Label")
        self.gridLayout_2.addWidget(self.Component2Label, 3, 0, 1, 1)
        self.Component2ComboBox1 = QtWidgets.QComboBox(self.MixerGroupBox)
        self.Component2ComboBox1.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Component2ComboBox1.setObjectName("Component2ComboBox1")
        self.Component2ComboBox1.addItem("")
        self.Component2ComboBox1.addItem("")
        self.gridLayout_2.addWidget(self.Component2ComboBox1, 3, 1, 1, 1)
        #################################
        self.Component2Slider = mixingRationSlider()
        self.Component2Slider.setParent(self.MixerGroupBox)
        self.Component2Slider.setCursor(
            QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Component2Slider.setMinimum(0)
        self.Component2Slider.setMaximum(100)
        self.Component2Slider.setSingleStep(10)
        self.Component2Slider.setProperty("value", 0)
        self.Component2Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Component2Slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Component2Slider.setObjectName("Component2Slider")
        self.gridLayout_2.addWidget(self.Component2Slider, 3, 2, 1, 3)
        self.Component2SliderStart = QtWidgets.QLabel(self.MixerGroupBox)
        self.Component2SliderStart.setObjectName("Component2SliderStart")
        self.gridLayout_2.addWidget(self.Component2SliderStart, 4, 2, 1, 1)
        self.Component2SliderEnd = QtWidgets.QLabel(self.MixerGroupBox)
        self.Component2SliderEnd.setAlignment(QtCore.Qt.AlignRight
                                              | QtCore.Qt.AlignTrailing
                                              | QtCore.Qt.AlignVCenter)
        self.Component2SliderEnd.setObjectName("Component2SliderEnd")
        self.gridLayout_2.addWidget(self.Component2SliderEnd, 4, 4, 1, 1)
        #################################
        self.Component2ComboBox2 = QtWidgets.QComboBox(self.MixerGroupBox)
        self.Component2ComboBox2.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Component2ComboBox2.setObjectName("Component2ComboBox2")
        self.Component2ComboBox2.addItem("")
        self.Component2ComboBox2.addItem("")
        self.Component2ComboBox2.addItem("")
        self.Component2ComboBox2.addItem("")
        self.Component2ComboBox2.addItem("")
        self.Component2ComboBox2.addItem("")
        self.gridLayout_2.addWidget(self.Component2ComboBox2, 4, 1, 1, 3)
        self.gridLayout_5.addWidget(self.MixerGroupBox, 0, 1, 1, 1)
        #################################

        #################################3
        self.Img2Groupbox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        self.Img2Groupbox.setFont(font)
        self.Img2Groupbox.setObjectName("Img2Groupbox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Img2Groupbox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Image2ComboBox = QtWidgets.QComboBox(self.Img2Groupbox)
        self.Image2ComboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Image2ComboBox.setObjectName("Image2ComboBox")
        self.Image2ComboBox.addItem("")
        self.Image2ComboBox.addItem("")
        self.Image2ComboBox.addItem("")
        self.Image2ComboBox.addItem("")
        self.gridLayout_3.addWidget(self.Image2ComboBox, 0, 1, 1, 1)
        self.Image2ViewerA = QtWidgets.QLabel(self.Img2Groupbox)
        self.Image2ViewerA.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Image2ViewerA.setObjectName("Image2ViewerA")
        self.gridLayout_3.addWidget(self.Image2ViewerA, 1, 0, 1, 1)
        # Display Img 2
        pixmap_img2 = QtGui.QPixmap(self.paths[1])
        pixmap_img2 = pixmap_img2.scaled(355, 300, QtCore.Qt.KeepAspectRatio)
        self.Image2ViewerA.setPixmap(pixmap_img2)
        #---------------------------------------------------------------
        ########################################################
        self.Image2ViewerB = QtWidgets.QLabel(self.Img2Groupbox)
        self.Image2ViewerB.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Image2ViewerB.setObjectName("Image2ViewerB")
        self.gridLayout_3.addWidget(self.Image2ViewerB, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.Img2Groupbox, 1, 0, 1, 1)
        self.OutputGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        self.OutputGroupBox.setFont(font)
        self.OutputGroupBox.setObjectName("OutputGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.OutputGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.viewer1 = QtWidgets.QLabel(self.OutputGroupBox)
        self.viewer1.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.viewer1.setObjectName("viewer1")
        self.viewer1.resize(50,50)
        self.gridLayout_4.addWidget(self.viewer1, 0, 0, 1, 1)
        self.viewer2 = QtWidgets.QLabel(self.OutputGroupBox)
        self.viewer2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.viewer2.setObjectName("viewer2")
        self.gridLayout_4.addWidget(self.viewer2, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.OutputGroupBox, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        # open images action
        self.openImageAction = newAction(MainWindow,os.path.realpath('../images/folder.png'),"openImageAction","Ctrl+O",self.openImages)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        # tool bar
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        self.toolBar.addAction(self.openImageAction)
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # progress bar
        self.progressBar = QtWidgets.QProgressBar(self.MixerGroupBox)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.hide()
        self.gridLayout_2.addWidget(self.progressBar,5,1,1,3)
        # hide data
        self.centralwidget.hide()
        # window = window.windowType()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.Component1Slider.valueChanged.connect(
            lambda: self.valuechange_slider(1))

        self.Component2Slider.valueChanged.connect(
            lambda: self.valuechange_slider(2))
        
        self.Component1Slider.mouseReleaseMethod = self.sliderValueReleased
        self.Component2Slider.mouseReleaseMethod = self.sliderValueReleased

        self.Component1ComboBox2.currentIndexChanged.connect(
            lambda: self.valuechange_Component1ComboBox2(1))
        self.Component2ComboBox2.currentIndexChanged.connect(
            lambda: self.valuechange_Component1ComboBox2(2))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Img1GroupBox.setTitle(_translate("MainWindow", "Image 1"))
        self.Image1ComboBox.setItemText(0, _translate("MainWindow",
                                                      "Magnitude"))
        self.Image1ComboBox.setItemText(1, _translate("MainWindow", "Phase"))
        self.Image1ComboBox.setItemText(2, _translate("MainWindow", "Real"))
        self.Image1ComboBox.setItemText(3, _translate("MainWindow",
                                                      "Imaginary"))
        self.MixerGroupBox.setTitle(_translate("MainWindow", "Mixer"))
        self.OutputLabel.setText(_translate("MainWindow", "Output to:"))
        self.OutputCombobox.setItemText(0, _translate("MainWindow",
                                                      "Output 1"))
        self.OutputCombobox.setItemText(1, _translate("MainWindow",
                                                      "Output 2"))
        self.Component1Label.setText(_translate("MainWindow", "Component 1:"))
        self.Component1ComboBox1.setItemText(
            0, _translate("MainWindow", "Image 1"))
        self.Component1ComboBox1.setItemText(
            1, _translate("MainWindow", "Image 2"))
        self.Component1ComboBox2.setItemText(
            0, _translate("MainWindow", components.magnitude))
        self.Component1ComboBox2.setItemText(1,
                                             _translate("MainWindow", components.phase))
        self.Component1ComboBox2.setItemText(2,
                                             _translate("MainWindow", components.real))
        self.Component1ComboBox2.setItemText(
            3, _translate("MainWindow", components.imaginary))
        self.Component1ComboBox2.setItemText(
            4, _translate("MainWindow", components.uniform_magnitude))
        self.Component1ComboBox2.setItemText(
            5, _translate("MainWindow", components.uniform_phase))
        #####################################################

        ########################################################
        self.Component2Label.setText(_translate("MainWindow", "Component 2:"))
        self.Component2ComboBox1.setItemText(
            0, _translate("MainWindow", "Image 1"))
        self.Component2ComboBox1.setItemText(
            1, _translate("MainWindow", "Image 2"))
        self.Component2ComboBox2.setItemText(
            0, _translate("MainWindow", components.magnitude))
        self.Component2ComboBox2.setItemText(1,
                                             _translate("MainWindow", components.phase))
        self.Component2ComboBox2.setItemText(2,
                                             _translate("MainWindow", components.real))
        self.Component2ComboBox2.setItemText(
            3, _translate("MainWindow", components.imaginary))
        self.Component2ComboBox2.setItemText(
            4, _translate("MainWindow", components.uniform_magnitude))
        self.Component2ComboBox2.setItemText(
            5, _translate("MainWindow", components.uniform_phase))
        #########################

        self.Component1SliderEnd.setText(_translate("MainWindow", "0%"))

        self.Component2SliderEnd.setText(_translate("MainWindow", "0%"))
        ###############################
        self.Img2Groupbox.setTitle(_translate("MainWindow", "Image 2"))
        ###################################################################
        # index of img2 combobox start from 4 to 7 to be unique
        ###################################################################
        self.Image2ComboBox.setItemText(0, _translate("MainWindow",
                                                      "Magnitude"))
        self.Image2ComboBox.setItemText(1, _translate("MainWindow", "Phase"))
        self.Image2ComboBox.setItemText(2, _translate("MainWindow", "Real"))
        self.Image2ComboBox.setItemText(3, _translate("MainWindow",
                                                      "Imaginary"))
        self.OutputGroupBox.setTitle(_translate("MainWindow", "Output"))
        ###################################################
        # linking is here
        # for Image1 and 2 components
        ####################################################
        self.Image1ComboBox.currentIndexChanged.connect(
            self.Update_img1Component)
        self.Image2ComboBox.currentIndexChanged.connect(
            self.Update_img2Component)
        #####################################################
        self.Component2ComboBox1.setCurrentIndex(1)
        self.Component2ComboBox2.setCurrentIndex(1)

    def Update_img1Component(self, component_indx):
        self.Update_img_componentV2(component_indx, "img1")

    def Update_img2Component(self, component_indx):
        self.Update_img_componentV2(component_indx, "img2")

    def Update_img_component(self, component_indx, var):
        pixmap_img1_comp = QtGui.QPixmap(self.paths[2])
        pixmap_img1_comp = pixmap_img1_comp.scaled(355, 300,
                                                   QtCore.Qt.KeepAspectRatio)

        if component_indx == 0:  # magnitude
            self.get_img_magnitude()
            self.Image1ViewerB.setPixmap(pixmap_img1_comp)
            self.Image1ViewerB.show()

        elif component_indx == 1:  # phase
            pass
        elif component_indx == 2:  # reals
            self.get_img_reals()
            self.Image1ViewerB.setPixmap(pixmap_img1_comp)
            self.Image1ViewerB.show()
        elif component_indx == 3:  # imaginary
            self.get_img_imgnary()
            self.Image1ViewerB.setPixmap(pixmap_img1_comp)
            self.Image1ViewerB.show()

    def Update_img_componentV2(self, component_indx, which_img):

        images = {"img1": 0, "img2": 1}
        img = images[which_img]

        if component_indx == 0:  # magnitude
            self.get_img_magnitude(img + 1)

        elif component_indx == 1:  # phase
            self.get_img_phase(img + 1)

        elif component_indx == 2:  # reals
            self.get_img_reals(img + 1)

        elif component_indx == 3:  # imaginary
            self.get_img_imgnary(img + 1)
        # new to this function
        pixmap_img1_comp = QtGui.QPixmap(self.paths[2])
        pixmap_img1_comp = pixmap_img1_comp.scaled(355, 300,
                                                   QtCore.Qt.KeepAspectRatio)
        pixmap_img2_comp = QtGui.QPixmap(self.paths[3])
        pixmap_img2_comp = pixmap_img2_comp.scaled(355, 300,
                                                   QtCore.Qt.KeepAspectRatio)

        viewers = [self.Image1ViewerB, self.Image2ViewerB]
        pixmaps = [pixmap_img1_comp, pixmap_img2_comp]

        viewers[img].setPixmap(pixmaps[img])
        viewers[img].show()

    def valuechange_slider(self, num_slider):
        if num_slider == 1:
            slider1value = self.Component1Slider.value()
            self.Component1SliderEnd.setText((f"{slider1value}%"))

        else:
            slider2value = self.Component2Slider.value()
            self.Component2SliderEnd.setText((f"{slider2value}%"))

    def sliderValueReleased(self,ev) : 
        self.mix()

    def valuechange_Component1ComboBox2(self, num_combox):
        if num_combox == 1:
            self.Component2ComboBox2.setCurrentText(components.opposite(self.Component1ComboBox2.currentText()))
        else:
            self.Component1ComboBox2.setCurrentText(components.opposite(self.Component2ComboBox2.currentText()))
        self.mix()
    def mix(self) : 
        # prgress bar setup
        self.progressBar.setValue(0)
        self.progressBar.show()
        imgage_1 = None
        imgage_2 = None
        # get images 
        if self.Component1ComboBox1.currentText() == "Image 1" : 
            imgage_1 = self.paths[0]
        if self.Component1ComboBox1.currentText() == "Image 2" : 
            imgage_1 = self.paths[1]
        if self.Component2ComboBox1.currentText() == "Image 1" :
            imgage_2 = self.paths[0]
        if self.Component2ComboBox1.currentText() == "Image 2" :
            imgage_2 = self.paths[1]
        #get components 
        component_1 = self.Component1ComboBox2.currentText()
        component_2 = self.Component2ComboBox2.currentText()
        # get mixing ration 
        mixingRatio_1 = int(self.Component1Slider.value())
        mixingRatio_2 = int(self.Component2Slider.value())
        # get output viewer
        if self.OutputCombobox.currentText() == "Output 1" :
            viewer = self.viewer1
        else :
            viewer = self.viewer2
        mixer = Mixer(imgage_1,imgage_2)
        mixer.start()
        mixer.signal.connect(self.updateProgressBar)
        data_after_Mixing = mixer.mix_with_the_opposite(component_1,mixingRatio_1,component_2,mixingRatio_2)
        plt.imshow(data_after_Mixing)
        plt.axis('off')
        pth = '../images/Output' + str(self.OutputCombobox.currentIndex() + 1) + '.png'
        plt.savefig(os.path.realpath(pth),bbox_inches='tight')
        output_image = QtGui.QPixmap(os.path.realpath(pth))
        viewer.setPixmap(output_image.scaled(viewer.width(),viewer.height(),QtCore.Qt.IgnoreAspectRatio))
        
        # hide progress bar
        self.progressBar.hide()
    def updateProgressBar(self,count) : 
        self.progressBar.setValue(count)

    def openImages(self) :
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        directory = dialog.getOpenFileNames(None,'select file',__file__,'image files (*.png *.jpg *.jpeg)')
        images = directory[0]
        if len(images) != 2 : 
            #error message for
            PromptError().error_message("please choose two images") 
            return
        # check the size of the two images 
        try : 
            mixer = Mixer(images[0],images[1])
            if not mixer.is_the_same_size() : 
                PromptError().error_message("please check that the two images has the same size")
                return
            # draw components and set the mixer up
            self.paths[0] = images[0] 
            self.paths[1] = images[1]
            self.Update_img1Component(self.Image1ComboBox.currentIndex())
            self.Update_img2Component(self.Image2ComboBox.currentIndex())
            #update mixer
            self.mix()
            # show data 
            self.centralwidget.show()
        except : 
            PromptError().error_message("please check that the two images has the same size")

    def resizeWindow(self,ev) : 
        if(self.viewer1.pixmap()) :
            self.viewer1.setPixmap(QtGui.QPixmap(os.path.realpath("../images/Output1.png")).scaled(self.viewer1.width(),self.viewer1.height(),QtCore.Qt.IgnoreAspectRatio))
        if(self.viewer2.pixmap()) :
            self.viewer2.setPixmap(QtGui.QPixmap(os.path.realpath("../images/Output2.png")).scaled(self.viewer2.width(),self.viewer2.height(),QtCore.Qt.IgnoreAspectRatio))
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = main_window()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.Update_img_componentV2(0, "img1")
    ui.Update_img_componentV2(0, "img2")
    MainWindow.show()
    sys.exit(app.exec_())
