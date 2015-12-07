from SimpleCV import *
import pdb
from face import *

# Counts the number of faces moving left right
cam = Camera(1)
display = Display()
haarCascadeFace = HaarCascade("face.xml")

face_old = []

total_left = 0
total_right = 0
while display.isNotDone():
  try:
    img = cam.getImage().flipHorizontal().scale(.5)
    faces = img.findHaarFeatures(haarCascadeFace)

    cur_count = len(faces)
    face_new = map(lambda x: Face(x), faces)

    # Find matches
    matches, unused_new, unused_old = match(face_new, face_old)
    dl = img.dl()
    
    for (i,j) in matches:
      diff = face_new[i].center - face_old[j].center
      pm = face_new[i].center
      
      upper_left = face_new[i].points[0]
      upper_right = face_new[i].points[1]
    
      already_counted = face_old[j].already_counted
    
      if (diff[0] + upper_left[0] < 0) and not already_counted:
        total_left += 1
        face_new[i].already_counted = True
      elif (diff[0] + upper_right[0] > 320) and not already_counted: 
        total_right += 1
        face_new[i].already_counted = True
      if diff[0] > 10:
        dl.text("Moving Right", location = (pm[0], pm[1]))
      elif diff[0] < -10:
        dl.text("Moving Left", location = (pm[0], pm[1]))

      # Update face_list
      face_old[j] = face_new[i]        

    for index in unused_old:
      face_old[index].last_seen += 1

    face_old = filter(lambda x: x.last_seen < 1, face_old)    
    for index in unused_new:
      face_old.append(face_new[index])

    dl.text("Count: %d" % cur_count, location = (130,30))
    dl.text("Total Right: %d" % total_right, location=(230,30))
    dl.text("Total Left: %d" % total_left, location=(30,30))
  
    for face in faces:
      face.draw()

    img.save(display)
  
  except KeyboardInterrupt:
    display.done = True

display.quit()
