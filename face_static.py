from SimpleCV import *
import sys
import time

filename = sys.argv[1]
display = Display()
haarCascadeFace = HaarCascade("face.xml")

img = Image(filename)
faces = img.findHaarFeatures(haarCascadeFace)
for face in faces:
  face.draw()

out = img.show()
while True:
  try:
    time.sleep(.3)
  except KeyboardInterrupt:
    break