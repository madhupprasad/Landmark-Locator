from PIL import Image
import random
import math

def extractor():
    nx = []
    ny = []
    c=0
    cc=0
    sam = Image.new("RGB",(1920,1017),"white")
    sam2 = sam.load()
    img = Image.open("qwerty.jpg")
    im = img.load()
    l1,w1 = img.size

    i = 0
    while i<w1:
        j = 0
        while j<l1:
            #cyan
            if im[j,i] == (0,255,255):
                im[j,i] = (255,255,255)
                sam2[j,i] = (0,0,0)
                ny.append(j)
                nx.append(i)
                c=c+1
                cc=cc+1
            j = j+1
        i = i+1

    a1=[]
    a2=[]
    a3=[]
    a4=[]
    a5=[]
    b1=[]
    b2=[]
    b3=[]
    b4=[]
    a5=[]
    b5=[]
    length = len(nx)
    for i in range(length):
        if i%2 == 0:
            a1.append(nx[i])
            b1.append(ny[i])
    for i in range(length/2):
        if i%2 == 0:
            a2.append(a1[i])
            b2.append(b1[i])
    for i in range(length/4):
        if i%2 == 0:
            a3.append(a2[i])
            b3.append(b2[i])
    for i in range(length/8):
        if i%2 == 0:
            a4.append(a3[i])
            b4.append(b3[i])

    return [l1,w1,len(a4),a4,b4]

#voronoi generator

def voronoi (width, height, num_cells ,nx,ny):
	image = Image.new("RGB",(width,height))
	putpixel = image.putpixel
	imgx,imgy = image.size
	nr = []
	ng = []
	nb = []
	for i in range(num_cells):

		nr.append(random.randrange(256))
		ng.append(random.randrange(256))
		nb.append(random.randrange(256))

	for y in range(imgy):
		for x in range(imgx):
			dmin = math.hypot(imgx-1, imgy-1)
			j = -1
			for i in range(num_cells):
				d = math.hypot(nx[i]-x, ny[i]-y)        #hypotenuse method
				putpixel((nx[i],ny[i]),(0,0,0))
				if d < dmin:
					dmin = d
					j = i
			putpixel((x, y), (nr[j], ng[j], nb[j]))

	image.save("final.jpg")

#driver

l1,w1,a,b,c = extractor()

voronoi(w1,l1,a,b,c)

#resize

def changeImageSize(image):
    newImage = image.resize((512, 512))
    return newImage

# Take two images for blending them together
image1 = Image.open("map.jpg")
image2 = Image.open("final.jpg")

# Make the images of uniform size
image3 = changeImageSize(image1)
image4 = changeImageSize(image2)

# Make sure images got an alpha channel
image5 = image3.convert("RGBA")
image6 = image4.convert("RGBA")

# alpha-blend the images with varying values of alpha
alphaBlended = Image.blend(image5,image6,alpha=.4)

# Display the alpha-blended images
alphaBlended.show()
