
    def drawSpectoForSignal1(self, GView, y, freq):

        f, t, Sxx = signal.spectrogram(y, freq)
        pyqtgraph.setConfigOptions(imageAxisOrder='row-major')

        win = GView
        p1 = win.addPlot()

        img = pyqtgraph.ImageItem()
        p1.addItem(img)
        hist = pyqtgraph.HistogramLUTItem()
        hist.setImageItem(img)
        win.addItem(hist)
        hist.setLevels(np.min(Sxx), np.max(Sxx))
        hist.gradient.restoreState({
            'mode':
            'rgb',
            'ticks': [(0.5, self.RGB_palette_1), (1.0, self.RGB_palette_2),
                      (0.0, self.RGB_palette_3)]
        })
        img.setImage(Sxx)
        img.scale(t[-1] / np.size(Sxx, axis=1), f[-1] / np.size(Sxx, axis=0))
        p1.setLimits(xMin=0, xMax=t[-1], yMin=0, yMax=f[-1])
        p1.setLabel('bottom', "Time", units='s')
        p1.setLabel('left', "Frequency", units='Hz')


        def check_palette(self):
            if self.combobox.currentText() == "palette1"
                self.RGB_Pallete_1 = (0, 182, 188, 255)
                self.RGB_Pallete_2 = (246, 111, 0, 255)
                self.RGB_Pallete_3 = (75, 0, 113, 255)
                self.drawSpectoForSignal1(self, GView, y, freq)
            

            if self.combobox.currentText() == "palette2"
                self.RGB_Pallete_1 = (108, 79, 60, 255)
                self.RGB_Pallete_2 = (100, 83, 148, 255)
                self.RGB_Pallete_3 = (0, 166, 140, 255
                self.drawSpectoForSignal1(self, GView, y, freq)

            if self.combobox.currentText() == "palette3"
                self.RGB_Pallete_1 = (191, 216, 51, 255)
                self.RGB_Pallete_2 = (188, 108, 167, 255)
                self.RGB_Pallete_3 = (235, 225, 223, 255
                self.drawSpectoForSignal1(self, GView, y, freq)

            if self.combobox.currentText() == "palette4"
                self.RGB_Pallete_1 = (219, 178, 209, 255)
                self.RGB_Pallete_2 = (147, 71, 66, 255)
                self.RGB_Pallete_3 = (108, 160, 220, 255
                self.drawSpectoForSignal1(self, GView, y, freq)


            if self.combobox.currentText() == "palette5"
                self.RGB_Pallete_1 = (236, 219, 83, 255)
                self.RGB_Pallete_2 = (227, 65, 50, 255)
                self.RGB_Pallete_3 = (219, 178, 209, 255)
                self.drawSpectoForSignal1(self, GView, y, freq)


