import h5py
import math
import numpy as np
import matplotlib.pyplot as plt
from gwpy.timeseries import TimeSeries

file = h5py.File("./output/default.hdf","r")
#print(file.keys())
# print(file['injection_parameters'].keys())
# print(file['injection_parameters']['h1_signal'])
x = file['injection_parameters']['scale_factor']
# print(x[0])
# print(np.sum(np.array(x))/5000)
# print(file['injection_samples']['h1_strain'])
# print(file['injection_parameters']['h1_signal'][0])
# print(file['injection_parameters']['h1_snr'][0])

def plotarr(arr):
  timeser = TimeSeries(arr)
  timeser.dt = 1/4096
  plt.plot(timeser)
  plt.show()

strain = np.array(file['injection_samples']['h1_strain'])
noise = np.array(file['injection_samples']['h1_noise'])
real_signal = file['injection_parameters']['h1_signal']
# # print(merged.shape)
# # print(noise.shape)
signal = strain - noise
# # s1 = merged - noise
# # #print(m1)
# plotarr(strain)
# plotarr(noise)
# plotarr(signal)
# plotarr(real_signal)
# plotarr(noise)
np.savetxt("bbh_strain.csv",strain, delimiter=" ")
np.savetxt("bbh_signal.csv",signal, delimiter=" ")
# plotarr(a)