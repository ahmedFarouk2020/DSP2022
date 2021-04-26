
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtCore
import sys
from numpy.fft import fft2, ifft2
from numpy import abs
import numpy as np
import png

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
        self.path1 = 'C:/Users/Farouk/Desktop/projects_VsCode/GUI/stinkbug1.png'
        # path of img2
        self.path2 = 'C:/Users/Farouk/Desktop/projects_VsCode/GUI/stinkbug2.png'
        # path of img1 component
        self.path3 = 'C:/Users/Farouk/Desktop/projects_VsCode/GUI/img1comp.png'
    
#########################################
    # After creating the omg component, you will pass the path of imgs to UI.py
    # what you craete inside UI.py(create img1 and 2) will be global for all 
    # the other labels
    # this file will be imported in UI.py
    def get_img_magnitude(self, img_number=1):

        arr_of_paths = [self.path1,self.path2] 
        # determine which img you will operate on
        path = arr_of_paths[img_number - 1]
        # get arrays of images
        self.image_arr=mpimg.imread(path)
        complex_arr = fft2(self.image_arr)
        # get magnitude of np complex array 
        magnitude = abs(complex_arr)
        img_arr = ifft2(magnitude)
        img_arr = [abs(x) for x in img_arr]
        print(img_arr) 
        #max_magnitude = np.amax(magnitude)
        # divid max value in array by all elements in the array ()
        #img_comp_mag = np.true_divide(magnitude,max_magnitude)
        #print(img_comp_mag)
        mpimg.imsave(self.path3,img_arr)
    def get_img_reals(self, img_number=1):

        arr_of_paths = [self.path1,self.path2] 
        # determine which img you will operate on
        path = arr_of_paths[img_number - 1]
        # get arrays of images
        self.image_arr=mpimg.imread(path)
        complex_arr = fft2(self.image_arr)
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
        mpimg.imsave(self.path3,img_arr)

    def get_img_imgnary(self, img_number=1):
        arr_of_paths = [self.path1,self.path2] 
        # determine which img you will operate on
        path = arr_of_paths[img_number - 1]
        # get arrays of images
        self.image_arr=mpimg.imread(path)
        complex_arr = fft2(self.image_arr)
        imagnary = [x.imag for x in complex_arr]
        img_arr = ifft2(imagnary)
        # get magnitude of array element to remove very small real numbers
        img_arr = [abs(x) for x in img_arr]
        #print(img_arr)
        #print(imagnary)
        #png.from_array(reals,mode="L").save("C:/Users/Farouk/Desktop/projects_VsCode/GUI/img1comp.png")
        # max_magnitude = np.amax(magnitude)
        # img_comp_mag = np.true_divide(magnitude,max_magnitude)
        # #print(img_comp_mag)
        mpimg.imsave(self.path3,img_arr)

        #print(magnitude)
        # fileHandle = open("img array.txt","w")
        # fileHandle.write(str(self.image_arr))
        # fileHandle.close()
        #print(self.image_arr)
        
        # # check that they have same size
        # if self.imageSize1 != self.imageSize1:
        #     # Error message
        #     self.error_message("Images sizes are different")

        # imgplot = plt.imshow(self.image_arr1)
        # plt.show()
        # imgplot = plt.imshow(self.image_arr2)
        # plt.show()

    def sav_img(self):
        lum_img = self.image_arr[:,:,0]
        imgplot = plt.imshow(lum_img)
        imgplot.set_cmap('hot')
        mpimg.imsave(self.path3,lum_img)
ob = DisplayImgComp()
ob.get_img_magnitude()
