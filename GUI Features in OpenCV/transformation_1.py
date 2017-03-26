import numpy as np 
import cv2
import matplotlib.image as mpimg
from matplotlib import pyplot as plt

img = cv2.imread("../Samples/image.jpg")
cv2.imshow('Normal',img)
k = cv2.waitKey(0)

lum_img = img[:,:,0]

if k == 27:
	cv2.destroyAllWindows()
elif k == ord('l'):	
	plt.imshow(lum_img)
	plt.xticks([]), plt.yticks([])
	plt.show()
elif k == ord('h'):
	hot_img = plt.imshow(lum_img, cmap = "hot")
	plt.xticks([]), plt.yticks([])
	plt.show() 
elif k == ord('n'):
	imgplot = plt.imshow(lum_img)
	imgplot.set_cmap('nipy_spectral')
	plt.xticks([]), plt.yticks([])
	plt.show()

