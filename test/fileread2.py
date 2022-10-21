import h5py
import math
import numpy as np
import matplotlib.pyplot as plt
from gwpy.timeseries import TimeSeries

file = h5py.File("./output/default.hdf","r")
keys = file.keys()
noise = file['injection_samples']['h1_noise']
print(noise[0])
signal = file['injection_samples']['h1_strain']
print(signal[0])

def plotarr(arr):
  timeser = TimeSeries(arr)
  timeser.dt = 1/4096
  plt.plot(timeser)
  plt.show()

#plotarr(noise[0])
#plotarr(noise[0]-signal[0])

for i in range(10):
  noise = file['injection_samples']['h1_noise'][i]
  signal = file['injection_samples']['h1_strain'][i]
  plotarr(noise-signal)
# h1s_arr = file['injection_parameters']['h1_signal'][0]
# h1m_arr = file['injection_samples']['h1_strain'][0]
# h1s = np.array(h1s_arr,dtype=np.float64)
# h1m = np.array(h1m_arr,dtype=np.float64)
# h1n = np.subtract(h1m,h1s,dtype=np.float64)
# t = np.subtract(h1m,h1n,dtype=np.float64)
#print(h1s)
#print(h1m)
#print(t)
# z = TimeSeries(h1s)
# z.dt = 1/4096
# z.name='Strain'
# qspec = z.q_transform()

def plot_data(data,lower_lim=0,upper_lim=4):
  exps = TimeSeries(data)
  exps.dt = 1/4096
  plt.plot(exps)
  #plt.xlim(lower_lim,upper_lim)
  plt.show()

def plot_q_tr(data):
  tdata = TimeSeries(data)
  tdata.dt=1/4096
  tdata.name='Strain'
  qspec = tdata.q_transform(outseg=(0,4))
  plot = qspec.plot(figsize=[8, 4])
  ax = plot.gca()
  ax.set_xscale('seconds')
  ax.set_yscale('log')
  ax.set_ylim(20, 500)
  ax.set_ylabel('Frequency [Hz]')
  ax.grid(True, axis='y', which='both')
  ax.colorbar(cmap='viridis', label='Normalized energy')
  plot.show()

def real_q_plot():
  t0 = 1126259462.4
  data = TimeSeries.read("/home/johngalt/Downloads/gwdata.hdf5",format='hdf5.losc')
  center = int(t0)
  data.plot()
  plt.show()
  data = data.crop(center-16, center+16)
  print("data reading done")

  qspecgram = data.q_transform(outseg=(1126259462.2, 1126259462.5))
  print("q transform done")
  print(data)
  # plot = qspecgram.plot(figsize=[8, 4])
  # ax = plot.gca()
  # ax.set_xscale('seconds')
  # ax.set_yscale('log')
  # ax.set_ylim(20, 500)
  # ax.set_ylabel('Frequency [Hz]')
  # ax.grid(True, axis='y', which='both')
  # ax.colorbar(cmap='viridis', label='Normalized energy')
  # plot.show()
#plot_data(h1n)
def f(x):
  if x:
    plot_q_tr(h1n)
  else:
    real_q_plot()

#f(1)
