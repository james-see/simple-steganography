# only works for python 27 due to stepic only supporting 27
from PIL import Image
import stepic

#for ch in "hello world!":
#    d = ord(ch)
#    b = bin(d)
#    print(ch, d, b)
try:
	imager = raw_input('full path of image location: ')
except:
	imager = input('full path of image location: ') # if using python 3.x
im = Image.open (imager)
im2 = stepic.encode(im, 'HELLO')
im2.save('stegtest.png',"PNG")
im1 = Image.open('stegtest.png')
s = stepic.decode(im1) 
print (s)
data = s.decode() 
print (data)