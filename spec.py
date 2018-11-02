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

intensityDifferences = []
maxIntensity = 0
avgIntensity = 0
minIntensity = -1

songLength = 4*len(samples)/sample_rate
for i in range(0, songLength-1, 1):
    index = i*len(times)/songLength
    #print(index)
    
    intensity = 0;
    
    for j in range(len(frequencies)):
        intensity += abs(spectrogram[j][index]-spectrogram[j][index+1])
    
    #print(intensity)
    if(intensity > maxIntensity):
        maxIntensity = intensity
        
    if(minIntensity -1 or intensity < minIntensity):
        minIntensity = intensity
        
    avgIntensity += intensity
    
    intensityDifferences.append(intensity)

    
    # avg = avg / len(frequencies)
    
    # if leftMax > avg:
    #     note = {}
    #     note["_time"] = i*0.25
    #     note["_lineIndex"] = random.randint(0,1)
    #     note["_lineLayer"] = random.randint(0,2)
    #     note["_type"] = 0
    #     note["_cutDirection"] = 8
    #     songJson["_notes"].append(note)
        
    # if rightMax > avg:
    #     note = {}
    #     note["_time"] = i*0.25
    #     note["_lineIndex"] = random.randint(2,3)
    #     note["_lineLayer"] = random.randint(0,2)
    #     note["_type"] = 1
    #     note["_cutDirection"] = 8
    #     songJson["_notes"].append(note)
  
avgIntensity = avgIntensity / len(intensityDifferences)
print(maxIntensity)
print(avgIntensity)
print(minIntensity)

for i in range(0, len(intensityDifferences), 1):
    maxDiff = abs(maxIntensity-intensityDifferences[i])
    avgDiff = abs(avgIntensity-intensityDifferences[i])
    minDiff = abs(minIntensity-intensityDifferences[i])
    
    if(intensityDifferences[i] > avgIntensity):
        note = {}
        note["_time"] = i*0.25
        note["_lineIndex"] = random.randint(2,3)
        note["_lineLayer"] = random.randint(0,2)
        note["_type"] = 1
        note["_cutDirection"] = 8
        songJson["_notes"].append(note)
        
for i in range(0, len(intensityDifferences), 4):
    maxDiff = abs(maxIntensity-intensityDifferences[i])
    avgDiff = abs(avgIntensity-intensityDifferences[i])
    minDiff = abs(minIntensity-intensityDifferences[i])
    
    if(intensityDifferences[i] <= avgIntensity*0.65):
        note = {}
        note["_time"] = i/4
        note["_lineIndex"] = random.randint(2,3)
        note["_lineLayer"] = random.randint(0,2)
        note["_type"] = 1
        note["_cutDirection"] = 8
        songJson["_notes"].append(note)

        
with open('Normal.json', 'w') as outfile:
    json.dump(songJson, outfile)
    
    