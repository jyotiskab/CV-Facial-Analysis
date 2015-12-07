from SimpleCV import *
import pdb
from face import *

# Counts the number of faces moving left right
cam = Camera(1)
display = Display()
haarCascadeFace = HaarCascade("face.xml")

face_old = []

while display.isNotDone():
  try:
    img = cam.getImage().flipHorizontal().scale(.5)
    faces = img.findHaarFeatures(haarCascadeFace)

    cur_count = len(faces)

    face_new = map(lambda x: Face(x), faces)

    # Map new faces to old
    matches, unused_new, unused_old = match(face_new, face_old)

    dl = img.dl()
    
    for (i,j) in matches:
      pm = face_new[i].center

      if face_old[j].area*1.10 < face_new[i].area:
        dl.text("Moving closer", location = (pm[0], pm[1]))
        #print "Moving Right"
      elif face_old[j].area*.90 > face_new[i].area:
        dl.text("Moving further", location = (pm[0], pm[1]))

      # Update face_list
      face_old[j] = face_new[i]        

    # Remove old faces from face list
    for index in unused_old:
      face_old[index].last_seen += 1

    face_old = filter(lambda x: x.last_seen < 1, face_old)    

    # Add to face list
    for index in unused_new:
      face_old.append(face_new[index])

    dl.text("Count: %d" % cur_count, location = (50,50))

    for face in faces:
      face.draw()

    img.save(display)
  
  except KeyboardInterrupt:
    display.done = True

display.quit()
