#import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import numpy as np
import json
import random

songJson = {}
songJson["_version"] = "1"
songJson["_beatsPerMinute"] = 120
songJson["_beatsPerBar"] = 16
songJson["_noteJumpSpeed"] = 10
songJson["_shuffle"] = 0
songJson["_shufflePeriod"] = 0.5
songJson["_events"] = []
songJson["_notes"] = []
songJson["_obstacles"] = []

sample_rate, samples = wavfile.read('song.wav')

print(len(samples)/sample_rate)
print(sample_rate)

frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

print(" ")
print(frequencies)
print(" ")
print(times)
print(" ")
print(spectrogram)

songLength = 4*len(samples)/sample_rate
for i in range(0, songLength, 1):
    index = i*len(times)/songLength
    print(index)
    freq = []
    
    avg = 0
    leftMax = spectrogram[0][index]
    rightMax = spectrogram[len(frequencies)-1][index]
    
    for j in range(len(frequencies)):
        avg += spectrogram[j][index]
        if j < len(frequencies)/2 and spectrogram[j][index] > leftMax:
            leftMax = spectrogram[j][index]
            
        if j >= len(frequencies)/2 and spectrogram[j][index] > rightMax:
            rightMax = spectrogram[j][index]

    
    avg = avg / len(frequencies)
    
    if leftMax > avg:
        note = {}
        note["_time"] = i*0.25
        note["_lineIndex"] = random.randint(0,1)
        note["_lineLayer"] = random.randint(0,2)
        note["_type"] = 0
        note["_cutDirection"] = 8
        songJson["_notes"].append(note)
        
    if rightMax > avg:
        note = {}
        note["_time"] = i*0.25
        note["_lineIndex"] = random.randint(2,3)
        note["_lineLayer"] = random.randint(0,2)
        note["_type"] = 1
        note["_cutDirection"] = 8
        songJson["_notes"].append(note)
        
with open('Normal.json', 'w') as outfile:
    json.dump(songJson, outfile)
    
    