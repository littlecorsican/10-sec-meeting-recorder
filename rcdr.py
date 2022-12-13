import soundcard as sc
import numpy
import atexit

speakers = sc.all_speakers()
default_speaker = sc.default_speaker()
mics = sc.all_microphones(include_loopback=True)

for i in range(len(mics)):
  try:
    print(f"{i} {mics[i].name}")
  except Exception as e:
    print(e)
    
chosenMic = input("Please input index of chosen mic, integer only")

array3d = []
array2d = []
def onExit():
  print("exit....replaying now")
  for data in array3d:
    for ndarray in data: #convert 3d array to 2d array , for smoother sound
      array2d.append(ndarray)
      #default_speaker.play(array2d/numpy.max(data), samplerate=48000)
      default_speaker.play(array2d, samplerate=48000)

atexit.register(onExit)

while True:
  print("recording...")
  data = mics[int(chosenMic)].record(samplerate=48000, numframes=48000)
  array3d.append(data)
  if len(array3d) > 10:
    array3d.pop(0)
