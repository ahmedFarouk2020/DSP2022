from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt
import struct
import soundfile as sf
#from playsound import playsound
import sys

class fourierTransform() : 
    def __init__(self) :
        
        self.data, self.sampling_rate = soundfileUtility.fn_ReadFile("WaveTest.wav")
        self.data_fft = np.fft.fft(self.data)
        # we will devide the range of freq into 10 ranges 
        # fmax = fsample / 2 
        self.maxFrequancy = self.sampling_rate / 2 
        #self.frequencies = (np.abs(self.data_fft[:int(self.maxFrequancy)]))
        self.frequencies = list( np.fft.fftfreq(len(self.data),1/self.sampling_rate) )
        bandWidthOfEachRange = int(self.maxFrequancy / 10)
        self.rangesOfFrequancy = [] # [[0,49],[50,99],...,[]] 10 elements
        start = 0
        end = bandWidthOfEachRange - 1
        for r in range(0,len(self.frequencies),bandWidthOfEachRange) : 
            self.rangesOfFrequancy.append([start,end])
            start = start + bandWidthOfEachRange
            end = end + bandWidthOfEachRange - 1
    
    # gain function takes 10 gains and it multiply each gain with the corresponding band  
    def gain(self,g1=1,g2=1,g3=1,g4=1,g5=1,g6=1,g7=1,g8=1,g9=1,g10=1) :
        self.dataAfterAmplification = self.data_fft
        for i in range(10) :
            bandWidth = self.rangesOfFrequancy[i]
            start = bandWidth[0]
            end = bandWidth[1]
            gain = locals()['g' + str(i + 1)]
            arr = self.data_fft[start:end + 1]
            # write positive and negative part part
            #print(start,end,self.maxFrequancy)
            for j in range(start,end + 1) : 
                self.dataAfterAmplification[j] = self.data_fft[j] * gain
                self.dataAfterAmplification[j + int(self.maxFrequancy)] = self.data_fft[j + int(self.maxFrequancy)] * gain
        
        return self.dataAfterAmplification
    
    # get complex-number array and do inverse transform on it
    def fn_InverceFourier(self, complex_arr):
        invrs = np.fft.ifft(complex_arr) #[21.0,0.00000j] so we remove imaginary part
        real_data = list(invrs.real) #sound file data
        return real_data

# offers utility need in sound file package
class soundfileUtility():
    # read wav file
    # returns sampling rate and sound data 
    @staticmethod
    def fn_ReadFile(file_name):
        data, samplerate = sf.read(file_name)
        return data, samplerate
        # data, samplerate = 0, 0
        # with open(file_name, 'r') as file:
        #     data, samplerate = sf.read(file)
        # return data, samplerate

    # create new sound file
    @staticmethod
    def fn_CreateSoundFile(file_name, arr_of_realNum, samplerate):
        sf.write(file_name, arr_of_realNum, int(samplerate))
        #sf.write(file_name, arr_of_realNum, int(samplerate))
        # with open(file_name, 'w') as file:
        #     sf.write(file, arr_of_realNum, int(samplerate))
        # return data, samplerate
    #  play sound file
    @staticmethod
    def fn_PlaySoundFile(file_name):
        playsound(file_name, block=False)

# it collect the data from sliders and passes them to fourierTransform.gain
class SlidersValues(fourierTransform):
    def __init__(self):
        super().__init__() # run init function of SliderValues
        self._value1 = 0
        self._value2 = 0
        self._value3 = 0
        self._value4 = 0
        self._value5 = 0
        self._value6 = 0
        self._value7 = 0
        self._value8 = 0
        self._value9 = 0
        self._value10 = 0
   
    def fn_slider1Value(self, value1=1):
        self._value1 = value1
        self.process()

    def fn_slider2Value(self, value2=1):
        self._value2 = value2
        self.process()

    def fn_slider3Value(self, value3=1):
        self._value3 = value3
        self.process()

    def fn_slider4Value(self, value4=1):
        self._value4 = value4
        self.process()

    def fn_slider5Value(self, value5=1):
        self._value5 = value5
        self.process()
  
    def fn_slider6Value(self, value6=1):
        self._value6 = value6
        self.process()

    def fn_slider7Value(self, value7=1):
        self._value7 = value7
        self.process()

    def fn_slider8Value(self, value8=1):
        self._value8 = value8
        self.process()

    def fn_slider9Value(self, value9=1):
        self._value9 = value9
        self.process()
  
    def fn_slider10Value(self, value10=1):
        self._value10 = value10
        self.process()
  
    def process(self): #(freq,complex_data,reals,time,np.abs(complex_data))
        complex_data = self.gain(self._value1,self._value2,self._value3,self._value4,
        self._value5,self._value6,self._value7,self._value8,self._value9,self._value10)
        reals = self.fn_InverceFourier(complex_data)
        time = [i for i in range(len(reals))]
        plt.plot(self.frequencies,np.abs(complex_data))
        plt.show()


class Ui_MainWindow(SlidersValues):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(900, 1000)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setTabletTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/eq.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.SpectrogramGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SpectrogramGroupBox.setFont(font)
        self.SpectrogramGroupBox.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.SpectrogramGroupBox.setObjectName("SpectrogramGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.SpectrogramGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.SpectrogramViewer = QtWidgets.QGraphicsView(self.SpectrogramGroupBox)
        self.SpectrogramViewer.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SpectrogramViewer.setStyleSheet("background-color:rgb(0,0,0)")
        self.SpectrogramViewer.setObjectName("SpectrogramViewer")
        self.gridLayout_2.addWidget(self.SpectrogramViewer, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.SpectrogramGroupBox, 0, 1, 3, 1)
        self.OriginalSignalGroupbox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.OriginalSignalGroupbox.setFont(font)
        self.OriginalSignalGroupbox.setObjectName("OriginalSignalGroupbox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.OriginalSignalGroupbox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.OriginalSignalViewer = QtWidgets.QGraphicsView(self.OriginalSignalGroupbox)
        self.OriginalSignalViewer.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.OriginalSignalViewer.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.OriginalSignalViewer.setObjectName("OriginalSignalViewer")
        self.gridLayout_5.addWidget(self.OriginalSignalViewer, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.OriginalSignalGroupbox, 0, 0, 1, 1)
        self.EditedSignalGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.EditedSignalGroupBox.setFont(font)
        self.EditedSignalGroupBox.setObjectName("EditedSignalGroupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.EditedSignalGroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.EditedSignalViewer = QtWidgets.QGraphicsView(self.EditedSignalGroupBox)
        self.EditedSignalViewer.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EditedSignalViewer.setStyleSheet("background-color:rgb(0,0,0)")
        self.EditedSignalViewer.setObjectName("EditedSignalViewer")
        self.gridLayout_3.addWidget(self.EditedSignalViewer, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.EditedSignalGroupBox, 2, 0, 1, 1)
        self.SignalEditorGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SignalEditorGroupBox.setFont(font)
        self.SignalEditorGroupBox.setObjectName("SignalEditorGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.SignalEditorGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label1 = QtWidgets.QLabel(self.SignalEditorGroupBox)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.gridLayout_7.addWidget(self.label1, 0, 0, 1, 1)
        self.label2 = QtWidgets.QLabel(self.SignalEditorGroupBox)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.gridLayout_7.addWidget(self.label2, 0, 1, 1, 1)
        self.label3 = QtWidgets.QLabel(self.SignalEditorGroupBox)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.gridLayout_7.addWidget(self.label3, 0, 2, 1, 1)
        self.label4 = QtWidgets.QLabel(self.SignalEditorGroupBox)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        self.gridLayout_7.addWidget(self.label4, 0, 3, 1, 1)
        self.label5 = QtWidgets.QLabel(self.SignalEditorGroupBox)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label5.setFont(font)
        self.label5.setObjectName("label5")
        self.gridLayout_7.addWidget(self.label5, 0, 4, 1, 1)
        self.label6 = QtWidgets.QLabel(self.SignalEditorGroupBox)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label6.setFont(font)
        self.label6.setObjectName("label6")
        self.gridLayout_7.addWidget(self.label6, 0, 5, 1, 1)
        self.label7 = QtWidgets.QLabel(self.SignalEditorGroupBox)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label7.setFont(font)
        self.label7.setObjectName("label7")
        self.gridLayout_7.addWidget(self.label7, 0, 6, 1, 1)
        self.label8 = QtWidgets.QLabel(self.SignalEditorGroupBox)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label8.setFont(font)
        self.label8.setObjectName("label8")
        self.gridLayout_7.addWidget(self.label8, 0, 7, 1, 1)
        self.label9 = QtWidgets.QLabel(self.SignalEditorGroupBox)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label9.setFont(font)
        self.label9.setObjectName("label9")
        self.gridLayout_7.addWidget(self.label9, 0, 8, 1, 1)
        self.label10 = QtWidgets.QLabel(self.SignalEditorGroupBox)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label10.setFont(font)
        self.label10.setObjectName("label10")
        self.gridLayout_7.addWidget(self.label10, 0, 9, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_7, 1, 0, 1, 10)
        self.Slider1 = QtWidgets.QSlider(self.SignalEditorGroupBox)
        self.Slider1.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Slider1.setMinimum(0)
        self.Slider1.setMaximum(5)
        self.Slider1.setSliderPosition(1)
        self.Slider1.setOrientation(QtCore.Qt.Vertical)
        self.Slider1.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Slider1.setTickInterval(1)
        self.Slider1.setObjectName("Slider1")
        self.gridLayout.addWidget(self.Slider1, 0, 0, 1, 1)
        self.Slider10 = QtWidgets.QSlider(self.SignalEditorGroupBox)
        self.Slider10.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Slider10.setMinimum(0)
        self.Slider10.setMaximum(5)
        self.Slider10.setOrientation(QtCore.Qt.Vertical)
        self.Slider10.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Slider10.setTickInterval(1)
        self.Slider10.setObjectName("Slider10")
        self.gridLayout.addWidget(self.Slider10, 0, 9, 1, 1)
        self.Slide6 = QtWidgets.QSlider(self.SignalEditorGroupBox)
        self.Slide6.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Slide6.setMinimum(0)
        self.Slide6.setMaximum(5)
        self.Slide6.setOrientation(QtCore.Qt.Vertical)
        self.Slide6.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Slide6.setTickInterval(1)
        self.Slide6.setObjectName("Slide6")
        self.gridLayout.addWidget(self.Slide6, 0, 5, 1, 1)
        self.Slider8 = QtWidgets.QSlider(self.SignalEditorGroupBox)
        self.Slider8.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Slider8.setMinimum(0)
        self.Slider8.setMaximum(5)
        self.Slider8.setOrientation(QtCore.Qt.Vertical)
        self.Slider8.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Slider8.setTickInterval(1)
        self.Slider8.setObjectName("Slider8")
        self.gridLayout.addWidget(self.Slider8, 0, 7, 1, 1)
        self.Slider3 = QtWidgets.QSlider(self.SignalEditorGroupBox)
        self.Slider3.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Slider3.setMinimum(0)
        self.Slider3.setMaximum(5)
        self.Slider3.setPageStep(10)
        self.Slider3.setOrientation(QtCore.Qt.Vertical)
        self.Slider3.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Slider3.setTickInterval(1)
        self.Slider3.setObjectName("Slider3")
        self.gridLayout.addWidget(self.Slider3, 0, 2, 1, 1)
        self.Slider2 = QtWidgets.QSlider(self.SignalEditorGroupBox)
        self.Slider2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Slider2.setToolTip("")
        self.Slider2.setMinimum(0)
        self.Slider2.setMaximum(5)
        self.Slider2.setOrientation(QtCore.Qt.Vertical)
        self.Slider2.setInvertedAppearance(False)
        self.Slider2.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Slider2.setTickInterval(1)
        self.Slider2.setObjectName("Slider2")
        self.gridLayout.addWidget(self.Slider2, 0, 1, 1, 1)
        self.Slider9 = QtWidgets.QSlider(self.SignalEditorGroupBox)
        self.Slider9.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Slider9.setMinimum(0)
        self.Slider9.setMaximum(5)
        self.Slider9.setOrientation(QtCore.Qt.Vertical)
        self.Slider9.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Slider9.setTickInterval(1)
        self.Slider9.setObjectName("Slider9")
        self.gridLayout.addWidget(self.Slider9, 0, 8, 1, 1)
        self.Slider5 = QtWidgets.QSlider(self.SignalEditorGroupBox)
        self.Slider5.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Slider5.setMinimum(0)
        self.Slider5.setMaximum(5)
        self.Slider5.setOrientation(QtCore.Qt.Vertical)
        self.Slider5.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Slider5.setTickInterval(1)
        self.Slider5.setObjectName("Slider5")
        self.gridLayout.addWidget(self.Slider5, 0, 4, 1, 1)
        self.Slider4 = QtWidgets.QSlider(self.SignalEditorGroupBox)
        self.Slider4.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Slider4.setMinimum(0)
        self.Slider4.setMaximum(5)
        self.Slider4.setProperty("value", 1)
        self.Slider4.setOrientation(QtCore.Qt.Vertical)
        self.Slider4.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Slider4.setTickInterval(1)
        self.Slider4.setObjectName("Slider4")
        self.gridLayout.addWidget(self.Slider4, 0, 3, 1, 1)
        self.Slider7 = QtWidgets.QSlider(self.SignalEditorGroupBox)
        self.Slider7.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Slider7.setMinimum(0)
        self.Slider7.setMaximum(5)
        self.Slider7.setOrientation(QtCore.Qt.Vertical)
        self.Slider7.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Slider7.setTickInterval(1)
        self.Slider7.setObjectName("Slider7")
###########################################################################
        # Linkage is here
###########################################################################
        self.Slider1.valueChanged[int].connect(self.fn_slider1Value)
        self.Slider2.valueChanged[int].connect(self.fn_slider2Value)
        self.Slider3.valueChanged[int].connect(self.fn_slider3Value)
        self.Slider4.valueChanged[int].connect(self.fn_slider4Value)
        self.Slider5.valueChanged[int].connect(self.fn_slider5Value)
        self.Slide6.valueChanged[int].connect(self.fn_slider6Value)
        self.Slider7.valueChanged[int].connect(self.fn_slider7Value)
        self.Slider8.valueChanged[int].connect(self.fn_slider8Value)
        self.Slider9.valueChanged[int].connect(self.fn_slider9Value)
        self.Slider10.valueChanged[int].connect(self.fn_slider10Value)

        self.gridLayout.addWidget(self.Slider7, 0, 6, 1, 1)
        self.gridLayout_4.addWidget(self.SignalEditorGroupBox, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Slider2, self.Slider3)
        MainWindow.setTabOrder(self.Slider3, self.Slider4)
        MainWindow.setTabOrder(self.Slider4, self.Slider5)
        MainWindow.setTabOrder(self.Slider5, self.Slide6)
        MainWindow.setTabOrder(self.Slide6, self.Slider7)
        MainWindow.setTabOrder(self.Slider7, self.Slider8)
        MainWindow.setTabOrder(self.Slider8, self.Slider9)
        MainWindow.setTabOrder(self.Slider9, self.Slider10)
        MainWindow.setTabOrder(self.Slider10, self.OriginalSignalViewer)
        MainWindow.setTabOrder(self.OriginalSignalViewer, self.EditedSignalViewer)
        MainWindow.setTabOrder(self.EditedSignalViewer, self.SpectrogramViewer)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Equalizer"))
        self.SpectrogramGroupBox.setTitle(_translate("MainWindow", "Spectrogram"))
        self.OriginalSignalGroupbox.setTitle(_translate("MainWindow", "Signal Before Editing"))
        self.EditedSignalGroupBox.setTitle(_translate("MainWindow", "Signal After Editing"))
        self.SignalEditorGroupBox.setTitle(_translate("MainWindow", "Signal Editor"))
        self.label1.setText(_translate("MainWindow", "TextLabel"))
        self.label2.setText(_translate("MainWindow", "TextLabel"))
        self.label3.setText(_translate("MainWindow", "TextLabel"))
        self.label4.setText(_translate("MainWindow", "TextLabel"))
        self.label5.setText(_translate("MainWindow", "TextLabel"))
        self.label6.setText(_translate("MainWindow", "TextLabel"))
        self.label7.setText(_translate("MainWindow", "TextLabel"))
        self.label8.setText(_translate("MainWindow", "TextLabel"))
        self.label9.setText(_translate("MainWindow", "TextLabel"))
        self.label10.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
