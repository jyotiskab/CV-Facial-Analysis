from SimpleCV import *
import sys

filename = sys.argv[1]

cam = Camera(1)
display = Display()
haarCascadeFace = HaarCascade("face.xml")

while display.isNotDone():
  img = cam.getImage().flipHorizontal().scale(.5)
  faces = img.findHaarFeatures(haarCascadeFace)
  for face in faces:
    face.draw()

  img.save(filename)
