from __future__ import division

import numpy as np
from scipy.misc import imread as im
from scipy.misc import toimage as to

img = im("/home/med/main/porn/blue/img0.jpg")


for x,y in enumerate(img):
	for a,b in enumerate(y):
		if type(y) != int:
			#for d,i in enumerate(b):
			#	print "divising ",img[x,a,d],type(img[x,a,d]) ,img[x,a,d]/10
			img[x,a,2] = img[x,a,2] / 255
		else:
			#print "divising ",img[x,a],type(img[x,a]) ,img[x,a]/10
			img[x,a] = img[x,a]+100

to(img).save('a.jpg')