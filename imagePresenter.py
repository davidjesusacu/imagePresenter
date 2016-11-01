from scipy.misc import imread, imresize, imsave

import numpy
import glob
import os
import sys


# "/Users/david/Desktop/Comparison/beatle/"  # current directory
def main(dir=None):
    if dir is None:
        dir = sys.argv[1]
    if os.path.exists(dir) == False:
        return
    ext = ".jpg"  # whatever extension you want
    distance = 5
    pathname = os.path.join(dir, "*" + ext)
    images = [imread(img)[:227, :227] for img in sorted(glob.glob(pathname))]

    height = sum(image.shape[0] for image in images) + distance * len(images)
    width = max(image.shape[1] for image in images)
    # output = numpy.zeros((height,width,3))
    output = numpy.ones((height, width, 3)) * 255
    y = 0
    for image in images:
        h, w, d = image.shape
        output[y:y + h, 0:w] = image
        y += (h + distance)

    imsave(dir + "collage.png", output)


if __name__ == "__main__":
    main()
