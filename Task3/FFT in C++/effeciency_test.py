import ctypes, time
from matplotlib import pyplot as plt
from numpy.ctypeslib import *
from ctypes import *
import numpy as np

class efficiencyTest():
    def __init__(self, real_input,real_output,img_output):
        # configure DFT library
        DFT = ctypes.cdll.LoadLibrary(r'C:\DSP2022\Task3\FFT in C++\DFT_pointer.so')
        DFT.dft2.restype = None
        DFT.dft2.argtypes = [ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                            ctypes.c_double,
                            ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                            ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")]
        self.dft = DFT.dft2
        # configure FFT library
        FFT = ctypes.cdll.LoadLibrary(r'C:\DSP2022\Task3\FFT in C++\FFT.cpp')
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
        self.error = []
        self.start = 0

    def FFT1(self):
        self.fft(self.input.size,self.input,self.real_output,self.img_output)
        self.FFTout = self.real_output+ 1j * self.img_output
        return self.FFTout

    def DFT1(self):
        self.dft(self.input,self.input.size,self.real_output,self.img_output)
        self.DFTout = self.real_output+ 1j * self.img_output
        return self.DFTout

    def startTimer(self):
        start = time.time() * 1000000
        return start

    def getElapsedTime(self, start):
        self.elapsedTime = time.time() * 1000000 - start
        return self.elapsedTime

    def getErrorArray(self,FFTout,DFTout):
        z = list(zip(FFTout,DFTout))
        self.error = [x-y for x,y in z]
        return self.error

    def drawErrorPlot(self):
        # the x axis (0 -> max index in error array)
        x = range(0,len(self.error),1)
        # the y axis (values of elements array)
        y = [x.real for x in self.error]
        plt.plot(x,y)
        plt.show()

    def drawPlot(self,N_values ,fft_time_array, dft_time_array):
        # the x axis (0 -> max index in error array)
        x = N_values
        # the y axis (values of elements array)
        y1 = fft_time_array
        y2 = dft_time_array
        # plot 
        plt.plot(x,y1,color="green",label="FFT") # FFT
        plt.plot(x,y2,color="red",label="DFT")  # DFT
        plt.legend()
        plt.show()
        

input_ = np.array([0.0,1.0,2.0,3.0])
real_output = np.zeros(input_.size)
img_output = np.zeros(input_.size)

a =efficiencyTest(input_,real_output,img_output)
# a.fft(input_.size,input_,real_output,img_output)

start = a.startTimer()
fftout = a.FFT1()
print(fftout)
fftTime = a.getElapsedTime(start)

start = a.startTimer()
dftout = a.DFT1()
print(dftout)
dftTime = a.getElapsedTime(start)
print(f" FFT time:{fftTime}ms \n DFT time:{dftTime}ms")

error = a.getErrorArray(dftout,fftout)
print(error)

a.drawErrorPlot()

N_values = [10, 100, 1000, 10000, 100000] # N-values
DFT_time = []
FFT_time = []
for x in N_values:
    input_ = np.array([5000.0 for i in range(x)])
    
    real_output = np.zeros(input_.size)
    img_output = np.zeros(input_.size)

    b = efficiencyTest(input_,real_output,img_output)
    # get dft time
    startDFT = b.startTimer()
    DFT1_out = b.DFT1()
    dft_time = b.getElapsedTime(startDFT)
    print(f"time for DFT: {dft_time}") 
    DFT_time.append(dft_time)
    #get fft time
    start = b.startTimer()
    FFT1_out = b.FFT1()
    fft_time = b.getElapsedTime(start)
    FFT_time.append(fft_time)

print(N_values)
print(FFT_time)
print(DFT_time)
b.drawPlot(N_values,FFT_time,DFT_time)


# FFT.fft(input_.size,input_,real_output,img_output)
# Data=real_output+ 1j * img_output

# print(np.round(Data, decimals=1))


