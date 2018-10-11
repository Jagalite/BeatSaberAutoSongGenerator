#import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import numpy as np

sample_rate, samples = wavfile.read('song.wav')

print(len(samples))
print(sample_rate)

frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate, nperseg=12800)

print(frequencies)
print(len(times))
print(spectrogram)

# for i in range(len(times)):
#     print(" ")
#     print(i)
#     print(len(spectrogram[0][times]))