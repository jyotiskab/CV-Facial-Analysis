from SimpleCV import *

# Tracks the faces in the image
cam = Camera(1)
display = Display()
haarCascadeFace = HaarCascade("face.xml")

while display.isNotDone():
  try:

    img = cam.getImage().flipHorizontal().scale(.5)
    faces = img.findHaarFeatures(haarCascadeFace)

    for face in faces:
      face.draw()

    img.save(display)

  except KeyboardInterrupt:
    display.done = True

display.quit()


