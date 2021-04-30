
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtCore
import sys
from numpy.fft import fft2, ifft2, fftshift
from numpy import abs
import numpy as np
import png
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class PromptError():
    def error_message(self, message):
        window = QtWidgets.QMessageBox()
        window.setWindowTitle("ERROR")
        window.setText(message)
        window.exec_()

class DisplayImgComp(PromptError):
    def __init__(self):
        # path of img1
        path1 = 'C:/Users/Farouk/Desktop/projects_VsCode/GUI/stinkbug1.png'
        # path of img2
        path2 = 'C:/Users/Farouk/Desktop/projects_VsCode/GUI/stinkbug2.png'
        # path of img1 component
        path3 = 'C:/Users/Farouk/Desktop/projects_VsCode/GUI/img1comp.png'
        # path of img1 component
        path4 = 'C:/Users/Farouk/Desktop/projects_VsCode/GUI/img2comp.png'
        self.paths = [path1,path2,path3,path4] 
        image_arr1=mpimg.imread(path1)
        image_arr2=mpimg.imread(path2)
        self.img_arrays = [image_arr1,image_arr2]
    
#########################################
    # After creating the omg component, you will pass the path of imgs to UI.py
    # what you craete inside UI.py(create img1 and 2) will be global for all 
    # the other labels
    # this file will be imported in UI.py
    def get_img_magnitude(self, img_number=1):

        # get arrays of images
        image_arr= self.img_arrays[img_number-1]
        complex_arr = fft2(image_arr)
        #shift the signal to origin
        #shifted_complex = fftshift(complex_arr)

        # get magnitude of np complex array 
        #magnitude = np.log(np.abs(shifted_sig))
        magnitude = abs(complex_arr)
        img_arr = ifft2(magnitude)
        img_arr = [x.real for x in img_arr]
        #print(img_arr) 
        #max_magnitude = np.amax(magnitude)
        # divid max value in array by all elements in the array ()
        #img_comp_mag = np.true_divide(magnitude,max_magnitude)
        #print(img_comp_mag)
        mpimg.imsave(self.paths[img_number+1],img_arr)

    def get_img_reals(self, img_number=1):

        
        # get arrays of images
        image_arr= self.img_arrays[img_number-1]
        complex_arr = fft2(image_arr)
        shifted_complex = fftshift(complex_arr)
        reals = [x.real for x in complex_arr]
        img_arr = ifft2(reals)
        # remove the imaginary part form final img array
        img_arr = [x.real for x in img_arr]
        #print(img_arr)
        #print(reals)
        #png.from_array(reals,mode="L").save("C:/Users/Farouk/Desktop/projects_VsCode/GUI/img1comp.png")
        # max_magnitude = np.amax(magnitude)
        # img_comp_mag = np.true_divide(magnitude,max_magnitude)
        # #print(img_comp_mag)
        mpimg.imsave(self.paths[img_number+1],img_arr)

    def get_img_imgnary(self, img_number=1):

        
        # get arrays of images
        image_arr= self.img_arrays[img_number-1]
        complex_arr = fft2(image_arr)
        shifted_complex = fftshift(complex_arr)
        imagnary = [x.imag for x in complex_arr]
        img_arr = ifft2(imagnary)
        # get magnitude of array element to remove very small real numbers
        img_arr = [x.real for x in img_arr]
        #print(img_arr)
        #print(imagnary)
        #png.from_array(reals,mode="L").save("C:/Users/Farouk/Desktop/projects_VsCode/GUI/img1comp.png")
        # max_magnitude = np.amax(magnitude)
        # img_comp_mag = np.true_divide(magnitude,max_magnitude)
        # #print(img_comp_mag)
        mpimg.imsave(self.paths[img_number+1],img_arr)

    def get_img_phase(self, img_number=1):
        
        # get an array of image
        image_arr= self.img_arrays[img_number-1]

        complex_arr = fft2(image_arr)
        shifted_complex = fftshift(complex_arr)
        # get phase component
        phase_spectrumA = np.angle(complex_arr)
        #self.save_in_file(phase_spectrumA)

        #magnitude_spectrumB = 20*np.log(np.abs(fshift1)) ****************************

        img_arr = ifft2(phase_spectrumA)

        #remove complex part
        img_arr = [x.real for x in img_arr]
        mpimg.imsave(self.paths[img_number+1],img_arr)
        
        # imgplot = plt.imshow(img_arr)
        # plt.show()
        # imgplot = plt.imshow(self.image_arr2)
        # plt.show()

###########################################################
# the below functions are for debugging (not used in the code)
############################################################
    def remove_file(path):
        os.remove(path)
    def save_in_file(array):
        fileHandle = open("img array.txt","w")
        fileHandle.write(str(array))
        fileHandle.close()
    def sav_img(self):
        lum_img = image_arr[:,:,0]
        imgplot = plt.imshow(lum_img)
        imgplot.set_cmap('hot')
        mpimg.imsave(self.path3,lum_img)

# ob = DisplayImgComp()
# ob.get_img_phase()
