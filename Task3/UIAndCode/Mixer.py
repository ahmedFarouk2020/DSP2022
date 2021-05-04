import matplotlib.image as mpimg
from numpy.fft import fft2, ifft2, fftshift
import numpy as np
import Components as components
from PyQt5 import QtCore, QtGui, QtWidgets
import time
class Mixer(QtCore.QThread) :
    signal = QtCore.pyqtSignal(int)
    def __init__(self,image1,image2) :
        super().__init__()
        self.progressCount = 0
        image1_data = mpimg.imread(image1)
        image2_data = mpimg.imread(image2)

        self.image1_data_fft = fft2(image1_data)
        self.image2_data_fft = fft2(image2_data)

        #reals
        self.image1_real = [x.real for x in self.image1_data_fft]
        self.image2_real = [x.real for x in self.image2_data_fft]

        #imaginary
        self.image1_imaginary = [x.imag for x in self.image1_data_fft] 
        self.image2_imaginary = [x.imag for x in self.image2_data_fft] 

        #phase
        self.image1_phase = np.angle(self.image1_data_fft)
        self.image2_phase = np.angle(self.image2_data_fft)
        #magnitude
        self.image1_magnitude = np.abs(self.image1_data_fft)
        self.image2_magnitude = np.abs(self.image2_data_fft)
        #uniform phase
        self.image1_uniform_phase = []

        for i in range(len(self.image1_phase)) : 
            arr2= []
            for j in range(len(self.image1_phase[i])) : 
                arr3 = []
                for g in range(len(self.image1_phase[i][j])) : 
                    arr3.append(0)
                arr2.append(arr3)
            self.image1_uniform_phase.append(arr2)

        self.image2_uniform_phase = list(self.image1_uniform_phase).copy()
        #uniform magnitude
        self.image1_uniform_magnitude = []
        for i in range(len(self.image1_phase)) : 
            arr2= []
            for j in range(len(self.image1_phase[i])) : 
                arr3 = []
                for g in range(len(self.image1_phase[i][j])) : 
                    arr3.append(1)
                arr2.append(arr3)
            self.image1_uniform_magnitude.append(arr2)
        self.image2_uniform_magnitude = list(self.image1_uniform_magnitude).copy()

    def mix_with_the_opposite(self,component_1,mixingRatio_1,component_2,mixingRatio_2) :
        # Ex : component 1 -> mag ; component 2 -> phase
        data_of_component_1 = getattr(self,"image1_" + component_1) # mag
        opposite_data_of_component_1 = getattr(self,"image1_" + components.opposite(component_1)) # phase
        data_of_component_2 = getattr(self,"image2_" + component_2) # phase
        opposite_data_of_component_2 = getattr(self,"image2_" + components.opposite(component_2)) # mag
        self.addToProgressCountAndEmit(10)
        #divide mixing ratio by 100 and multiply it by the length to get the desired data
        desired_length_of_data_1 = int((mixingRatio_1 / 100 ) * len(data_of_component_1)) # 480
        desired_length_of_data_2 = int((mixingRatio_2 / 100 ) * len(data_of_component_2)) # 0
        self.addToProgressCountAndEmit(10)
        #get desired data
        desired_data_of_component_1 = data_of_component_1[0:desired_length_of_data_1] # all
        desired_data_of_component_2 = data_of_component_2[0:desired_length_of_data_2] # 
        desired_opposite_data_of_component_1 = opposite_data_of_component_1[desired_length_of_data_2:]
        desired_opposite_data_of_component_2 = opposite_data_of_component_2[desired_length_of_data_1:]
        self.addToProgressCountAndEmit(10)
        # pre mixing data 
        final_data_of_component_1 = list(desired_data_of_component_1) + list(desired_opposite_data_of_component_2)
        final_data_of_component_2 = list(desired_data_of_component_2) + list(desired_opposite_data_of_component_1)
        self.addToProgressCountAndEmit(10)
        # ex mix("real",60)
        # n^3 
        data_after_mixing = []
        if component_1 == components.real : 
            imaginary_part = np.array(final_data_of_component_2) * 1j
            data_after_mixing = np.add(final_data_of_component_1,imaginary_part)
        elif component_1 == components.imaginary : 
            imaginary_part = np.array(final_data_of_component_1) * 1j
            data_after_mixing = np.add(final_data_of_component_2,imaginary_part)
        elif component_1 == components.magnitude or component_1 == components.uniform_magnitude : 
            imaginary_part = np.array(final_data_of_component_2) * 1j
            exp_part = np.exp(imaginary_part)
            data_after_mixing = np.multiply(final_data_of_component_1,exp_part)
        else : 
            imaginary_part = np.array(final_data_of_component_1) * 1j
            exp_part = np.exp(imaginary_part)
            data_after_mixing = np.multiply(final_data_of_component_2,exp_part)
        self.addToProgressCountAndEmit(30)
        original_data_after_mixing = ifft2(data_after_mixing)
        self.addToProgressCountAndEmit(10)
        original_data_after_mixing = [ x.real for x in original_data_after_mixing]
        self.addToProgressCountAndEmit(10)
        data = np.int32(original_data_after_mixing)
        self.addToProgressCountAndEmit(10)
        return data 
    def run(self) :
        print("starting mix ... ")
    def addToProgressCountAndEmit(self,count) :
        self.progressCount += count 
        self.signal.emit(self.progressCount)



