# only works for python 27 due to stepic only supporting 27
from PIL import Image
import stepic

imager = input('full path of image location: ')  # if using python 3.x
im = Image.open(imager)
encodeddata = input('message to hide: ').encode()
# TODO add ability to also ask for a file to hide
# datatoencode = open('test.txt', 'rb').read()
im2 = stepic.encode(im, encodeddata)
im2.save('stegtest.png', "PNG")
im1 = Image.open('stegtest.png')
s = stepic.decode(im1)
print(f"The message you hid in the image: {s}")
