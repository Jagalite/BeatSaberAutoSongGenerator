from pydub import AudioSegment
import json
import random

song = AudioSegment.from_mp3("song.mp3")

ninf = -float("inf")

avg = 0

time = 500
segments = len(song)/time

for i in range(0, len(song), segments):
    loudness = song[i:i+segments].dBFS
    if(loudness != ninf):
        avg += loudness

avg = avg/time
print("@@@@@@@@@")
print(avg)
print("@@@@@@@@@")

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
    
for i in range(0, len(song), segments):
    loudness = song[i:i+segments].dBFS
    if((i > float(1000)) and loudness <= avg*0.75):
        print(i/float(1000))
        note = {}
        note["_time"] = i/float(1000)
        note["_lineIndex"] = random.randint(0,3)
        note["_lineLayer"] = random.randint(0,2)
        note["_type"] = random.randint(0,1)
        note["_cutDirection"] = 8
        songJson["_notes"].append(note)

with open('Normal.json', 'w') as outfile:
    json.dump(songJson, outfile)


song.export("song.ogg", format="ogg")
