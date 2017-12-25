import numpy as np
from skimage.draw import polygon, ellipse
from skimage.viewer import ImageViewer
import constants as const

# Drawing functions
def drawTriangle(x, y, # Top left corner coordinates
				h, w, # height and width of bounding box of triangle
				direc=0): # direction of orientation of tip of triangle
							# (0 is right, 1 is down, 2 is left, 3 is up)
	if direc==2:
		y+=w
	elif direc==3:
		x+=h

	if direc%2==0:
		r = np.array([x, x+h, x+h/2, x])
		c = np.array([y, y, y + w - 2*w*direc/2, y])
	else:
		r = np.array([x, x, x + h - 2*h*(direc-1)/2, x])
		c = np.array([y, y+w, y + w/2, y])

	return polygon(r, c)

def drawRect(x, y, # Top left corner coordinates
				h, w): # height and width of rectangle
	r = np.array([x, x+h, x+h, x, x])
	c = np.array([y, y, y + w, y+w, y])

	return polygon(r, c)

def drawSquare(x, y, # Top left corner coordinates
				h, w=0): # height of square
	return drawRct(x,y,h,h)


def drawEllipse(x, y, # Top left corner coordinates
				h, w, # height and width of bounding box of ellipse
				rotDeg=0.0): # degrees of rotation of ellipse
	return ellipse(x+h/2, y+w/2, h/2, w/2, shape = (const.H, const.W),
				rotation=np.deg2rad(rotDeg)) # rotation not used ever


def drawCircle(x, y, # Top left corner coordinates
				h, w=0): # height and width of bounding box of ellipse
				
	return drawEllipse(x,y,h,h)

def inRange(coords):
	return ((coords >= 1) & (coords < const.H-1)).all() # since square image

# Image generations
def createRandomImage(alldiff=True, # If the shapes are all of different colors and shapes
					nshapes = 3, # Number of shapes in image
					overlap=False): # if shapes are allowed to overlap

	H = const.H
	W = const.W
	k=0

	colors = range(3)


	while ((not overlap) and alldiff):
		k+=1
		img = np.zeros((H, W, 3), dtype=np.uint8)
		translated_img = np.zeros((H, W, 3), dtype=np.uint8)
		
		# topLefts = np.random.randint(1,109,size=(3,2,))
		# shapeSizes = np.random.randint(10,25,size=(3,2,))

		topLefts = np.random.randint(1,58,size=(3,2,))
		shapeSizes = np.random.randint(10,20,size=(3,2,))
		shapeSizes[2,0] = shapeSizes[2,1] # for the cirle
		np.random.shuffle(colors)
		triangDir = np.random.randint(0,4)

		translationDir = np.random.randint(0,4)
		translationNum = np.random.randint(0,3)

		topLeftDiffs = np.zeros((3,2), dtype=np.int32)
		topLeftDiffs[translationNum,(translationDir+1)%2] = const.transAmt * (1-2*int(translationDir>1))
		topLeftsNew = topLefts + topLeftDiffs

		if inRange(topLefts) and inRange(topLefts + shapeSizes) and inRange(topLeftsNew) and inRange(topLeftsNew + shapeSizes):

			rr, cc = drawRect(topLefts[0,0],topLefts[0,1],shapeSizes[0,0],shapeSizes[0,1])
			img[rr,cc,colors[0]] = 1

			rr, cc = drawTriangle(topLefts[1,0],topLefts[1,1],shapeSizes[1,0],shapeSizes[1,1], triangDir)
			img[rr,cc,colors[1]] = 1

			rr, cc = drawCircle(topLefts[2,0],topLefts[2,1],shapeSizes[2,0],shapeSizes[2,1])
			img[rr,cc,colors[2]] = 1



			rr, cc = drawRect(topLeftsNew[0,0],topLeftsNew[0,1],shapeSizes[0,0],shapeSizes[0,1])
			translated_img[rr,cc,colors[0]] = 1

			rr, cc = drawTriangle(topLeftsNew[1,0],topLeftsNew[1,1],shapeSizes[1,0],shapeSizes[1,1], triangDir)
			translated_img[rr,cc,colors[1]] = 1

			rr, cc = drawCircle(topLeftsNew[2,0],topLeftsNew[2,1],shapeSizes[2,0],shapeSizes[2,1])
			translated_img[rr,cc,colors[2]] = 1


			if (not (np.sum(img,axis=2)>1).any()) and (not (np.sum(translated_img,axis=2)>1).any()): # not overlaping
				break

	color_changed = colors[translationNum]
	shape_changed = translationNum
	dir_changed = translationDir

	return img, translated_img, color_changed, shape_changed, dir_changed


def saveManyImages(nexamples = 4, # number of examples to save
					alldiff=True, # If the shapes are all of different colors and shapes
					nshapes = 3, # Number of shapes in image
					overlap=False): # if shapes are allowed to overlap

	original_imgs = np.zeros((nexamples, const.H, const.W, 3), dtype=np.uint8)
	translated_imgs = np.zeros((nexamples, const.H, const.W, 3), dtype=np.uint8)
	sentences = np.zeros((nexamples, 3+3+4), dtype=np.uint8)

	for i in range(nexamples):
		img, translated_img, color_changed, shape_changed, dir_changed = createRandomImage(alldiff, nshapes, overlap)
		# print color_changed, shape_changed, dir_changed 
		original_imgs[i] = img
		translated_imgs[i] = translated_img

		sentences[i,[color_changed, 3+shape_changed, 6+dir_changed]] = 1

	np.save('original_imgs_64', original_imgs)
	np.save('translated_imgs_64', translated_imgs)
	np.save('sentences_64', sentences)





#viewing function
def displayImage(img):
	viewer = ImageViewer(img*255)
	viewer.show()



