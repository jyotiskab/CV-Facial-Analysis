from SimpleCV import *
import matplotlib.pyplot as plt
import numpy as np

# Tracks the faces, and provide plot of user count

# Set up Camera/Display
cam = Camera(1)
display = Display()
haarCascadeFace = HaarCascade("face.xml")

# Set up auxiliary plot
plt.ion()
plt.show()

fig=plt.figure()
ax = fig.add_subplot(111)

# Global variables
total_sum = 0.0
i = 1

while display.isNotDone():
  try:
    img = cam.getImage().flipHorizontal().scale(.5)
    faces = img.findHaarFeatures(haarCascadeFace)

    cur_count = len(faces)
    total_sum += cur_count
    mean = total_sum / i

    # Update drawing layer
    dl = img.dl()
    dl.text("Count: %d" % cur_count, location = (50,50))

    # Update matplotlib figure
    ax.scatter(i, cur_count)
    ax.axes.axhline(y=mean)
    plt.draw()

    # Delete Avg line
    del ax.axes.lines[-1]

    for face in faces:
      face.draw()

    img.save(display)
    i += 1

  except KeyboardInterrupt:
    display.done = True

display.quit()
