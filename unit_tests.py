import numpy as np
from skimage.draw import polygon, ellipse
from skimage.viewer import ImageViewer
import constants as const
from make_images import *

# H = const.H
# W = const.W

# img = np.zeros((H, W, 3), dtype=np.uint8)
# r = np.array([1, 2, 8, 1])
# c = np.array([1, 7, 4, 1])
# rr, cc = polygon(r, c)
# img[rr, cc] = 1
# img

# Triangle tests
# i=0
# rr, cc = drawTriangle(20, 20, 30, 50, 0)
# img[rr,cc,i] = 255
# i+=1

# rr, cc = drawTriangle(80, 80, 30, 100, 1)
# img[rr,cc,i] = 255
# i+=1

# rr, cc = drawTriangle(120, 20, 10, 50, 2)
# img[rr,cc,i] = 255
# i+=1

# rr, cc = drawTriangle(20, 120, 100, 50, 3)
# img[rr,cc,2] = 255
# i+=1



# Rectangle tests
# rr, cc = drawRct(50,50,100, 20)
# img[rr,cc,1] = 255

# rr, cc = drawRct(100,100,10, 50)
# img[rr,cc,2] = 255



# Rectangle tests
# rr, cc = drawRect(25,25,15,10)
# img[rr,cc,1] = 255


# rr, cc = drawTriangle(50,50,25, 25,2)
# img[rr,cc,0] = 255

# rr, cc = drawEllipse(80,50,25, 25)
# img[rr,cc,0] = 255

colors = ["Red", "Green", "Blue"]
shapes = ["Rectangle", "Triangle", "Ellipse"]
directions = ["right", "down", "left", "up"]

# for i in range(20):
# 	img, ti, color_changed, shape_changed, dir_changed = createRandomImage()

# 	print colors[color_changed], shapes[shape_changed], directions[dir_changed]
# 	displayImage(img)
# 	displayImage(ti)

# saveManyImages(100000)


