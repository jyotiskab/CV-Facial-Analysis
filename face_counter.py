from SimpleCV import *
import datetime

# Counts the people and prints the number
cam = Camera(1)
display = Display()
haarCascadeFace = HaarCascade("face.xml")

# Make the file
f = open('counter.txt','w')

while display.isNotDone():
  try:
    img = cam.getImage().flipHorizontal().scale(.5)
    faces = img.findHaarFeatures(haarCascadeFace)

    cur_count = len(faces)

    # Update drawing layer
    dl = img.dl()
    dl.text("Count: %d" % cur_count, location = (50,50))
    f.write('%s, %d\n' % (str(datetime.datetime.now()), cur_count))

    for face in faces:
      face.draw()

    img.save(display)
  
  except KeyboardInterrupt:
    display.done = True

display.quit()
f.close()

