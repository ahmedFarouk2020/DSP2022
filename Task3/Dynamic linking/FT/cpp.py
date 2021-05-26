import ctypes, time
from matplotlib import pyplot as plt
from numpy.ctypeslib import *
from ctypes import *
import numpy as np
import os

#path1 = os.path.realpath('../FT/shared_lib/DFT_FFT2.so')
class efficiencyTest():
    def __init__(self, real_input,real_output,img_output):
        # configure DFT library
        DFT = ctypes.cdll.LoadLibrary(os.path.realpath('../GUI/Dynamic linking/FT/shared_lib/DFT_FFT2.so'))
        DFT.dft.restype = None
        DFT.dft.argtypes = [ ctypes.c_double,
                             ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                             ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                             ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")]
        self.dft = DFT.dft
        # configure FFT library
        FFT = ctypes.cdll.LoadLibrary(os.path.realpath('../GUI/Dynamic linking/FT/shared_lib/DFT_FFT2.so'))
        FFT.fft.restype = None
        FFT.fft.argtypes = [   ctypes.c_double,
                                ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                                ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                                ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")]
        
        self.fft = FFT.fft

        #set parameters
        self.input = real_input
        self.real_output = real_output
        self.img_output = img_output
        self.DFTout = []
        self.FFTout = []

    def change_input(self,input,real_output,img_output):
        self.input = input
        self.real_output = real_output
        self.img_output = img_output

    def FFT1(self):
        self.fft(self.input.size,self.input,self.real_output,self.img_output)
        self.FFTout = self.real_output+ 1j * self.img_output
        

    def DFT1(self):
        self.dft(self.input.size,self.input,self.real_output,self.img_output)
        self.DFTout = self.real_output+ 1j * self.img_output
        

    def startTimer(self):
        start = time.time() * 1000000
        return start

    def getElapsedTime(self, start):
        elapsedTime = time.time() * 1000000 - start
        return elapsedTime

    def getErrorArray(self,FFTout,DFTout):
        z = list(zip(FFTout,DFTout))
        error = [np.abs(np.square(np.subtract(x,y)).mean()) for x,y in z]
        return error

    def drawErrorPlot(self):
        # the x axis (0 -> max index in error array)
        x = range(0,len(self.error),1)
        # the y axis (values of elements array)
        y = [x.real for x in self.error]
        
        plt.ylim((-2,6))

        plt.xlabel("N-values")
        plt.ylabel("Error")
        plt.plot(x,y)
        plt.show()
    @staticmethod
    def drawPlot(N_values=None,ERROR_FLAG=1,error=None,y_axis1=None,y_axis2=None,xlabel="",
                    ylabel="",legend1="", legend2=""):

        if ERROR_FLAG == 1:
            # the x axis (0 -> max index in error array)
            x = range(0,len(error),1)
            # the y axis (values of elements array)
            y = [x.real for x in error]
            plt.ylim((-2,6))
            plt.plot(x,y)
        else:
            # the x axis (0 -> max index in error array)
            x = N_values
            plt.ylim((0,10000))
            plt.plot(x,y_axis1,color="green",label=legend1) # FFT
            plt.plot(x,y_axis2,color="red",label=legend2)  # DFT
        # labels
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        # plot 
        plt.legend()
        plt.show()
        
