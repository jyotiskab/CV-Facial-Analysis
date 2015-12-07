import os
import numpy as np
import pdb
# Maybe reverse the order of the loops to attach
# things to the face_list
def match(face_new, face_old):

	
	matches = []
	total_new = set(range(len(face_new)))
	total_old = set(range(len(face_old)))
	used_new = set()
	used_old = set()

	for (j,face_anchor) in enumerate(face_old):
		min_center_diff = 1000
		min_index = -1

		for (i,new_face) in enumerate(face_new):
			size_ratio = (new_face.area/face_anchor.area)
			center_diff = np.sum(np.abs(new_face.center - face_anchor.center))
			#print size_ratio
			#print center_diff

			if ( 0.5 < size_ratio < 2) and \
				 (center_diff < 120) and \
				 (center_diff < min_center_diff) and \
				 (i not in used_new):
				min_center_diff = center_diff
				min_index = i

		if not min_index == -1:
			used_old.add(j)
			used_new.add(min_index)
			matches.append((min_index,j))

	return matches, total_new - used_new, total_old - used_old

class TestFace:
	def __init__(self, x, y):
		self.center = np.array([x,y])
		self.area = 1


class Face:
	def __init__(self, face_feature):
		self.center = np.array([face_feature.x, face_feature.y])
		self.points = face_feature.points
		self.area = float(face_feature.area())
		self.last_seen = 0
		self.already_counted = False


	def __repr__(self):
		return "Center: %s| Already counted: %s" % (str(self.center), str(self.already_counted))
