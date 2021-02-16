# only works for python 27 due to stepic only supporting 27
from PIL import Image
import stepic

# get image path (use pngs/original.png)
imager = input('full path of image location: ') 
# open image
im = Image.open(imager)
# get data to encode and hide
encodeddata = input('message to hide: ').encode()
# TODO add ability to also ask for a file to hide
# datatoencode = open('test.txt', 'rb').read()
# hide the data in the image
im2 = stepic.encode(im, encodeddata)
# save the result
im2.save('stegtest.png', "PNG")
# open the result
im1 = Image.open('stegtest.png')
# decode and print the message
s = stepic.decode(im1)
print(f"The message you hid in the image: {s}")
