import numpy as np
from cpp import efficiencyTest as ET

input_ = np.array([1.0,2.0,5.0,6.0,4.0,24.0,5.0,4.0])
real_output = np.zeros(input_.size)
img_output = np.zeros(input_.size)

a =ET(input_,real_output,img_output)

a.FFT1()
a.DFT1()

# Draw Error vs number of samples
error = a.getErrorArray(a.DFTout,a.FFTout)
ET.drawPlot(error=error,xlabel="# of samples",ylabel="Error")

N_values = [2**x for x in range(2,9,1)] # list of "Number of samples N"
DFT_time = []
FFT_time = []

for x in N_values:
    # get random input
    input_ = np.array([float(j) for j in range(x)])
    # fill output with zeros
    real_output = np.zeros(input_.size)
    img_output = np.zeros(input_.size)

    a.change_input(input_,real_output,img_output)

    # fill dft time array
    startDFT = a.startTimer()
    DFT1_out = a.DFT1()
    dft_time = a.getElapsedTime(startDFT)
    DFT_time.append(dft_time)

    # fill fft time array
    start1 = a.startTimer()
    FFT1_out = a.FFT1()
    fft_time = a.getElapsedTime(start1)
    FFT_time.append(fft_time)


ET.drawPlot(N_values=N_values,ERROR_FLAG=0,y_axis1=DFT_time,y_axis2=FFT_time,xlabel="# of samples"
,ylabel="Time(us)",legend1="DFT",legend2="FFT")