import sys, os, struct, binascii, ntpath
from PIL import Image

def clean(path):
	head, tail = ntpath.split(path)
	return tail or ntpath.basename(head)

def openImage(fn):
	inFile = Image.open(fn)
	pixels = inFile.load()
	return pixels, (inFile.size[0], inFile.size[1])

def encodeData(data, dimensions, encode):

	encode_Data = []
	edit = data
	j = 0

	for char in encode:
		encode_Data.append('{:08b}'.format(ord(char)))
	encode_Data = ''.join(encode_Data)

#	print encode_Data
#	print 8*len(encode_Data), "bytes needed."
#	print (8*3)*(dimensions[1]+dimensions[0]), "bytes available."

	i = 0
	for y in range(dimensions[1]):
			for x in range(dimensions[0]):
				if i < len(encode_Data):
#					print edit[x,y]
					i += 1

	if (8*3)*(dimensions[1]+dimensions[0]) > 8*len(encode_Data):
		for y in range(dimensions[1]):
			for x in range(dimensions[0]):
					for i in range(3):
						if j < len(encode_Data):
							tmp = list(edit[x,y])
							tmp[i] = ((tmp[i] & 0xfe), (tmp[i] | 0x1))[int(encode_Data[j])]
							j += 1
							edit[x,y] = tuple(tmp)
						else:
							break
		return data

	else:
		print "You can only store ",  (3*(dimensions[1]+dimensions[0]))/3, "characters in this image!"

#	print '-'*40
#	i = 0
#	for y in range(dimensions[1]):
#			for x in range(dimensions[0]):
#				if i < len(encode_Data):
#					print edit[x,y]
#					i += 1
#	print '-'*40

def eom():
	print "\nEnd of message.\n"
	exit(0)

def valid(input):
	if input in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=!@#$%^&*()_+~'\";:,./<>[]{}\\| \t\b\r":
		return False
	elif input == "`":
		eom()
	else:
		return True

def decodeData(data, dimensions):
	decode_Data = []
	tmp = ""

	for y in range(dimensions[1]):
		for x in range(dimensions[0]):
				for i in range(3):
					tmp += str('{:08b}'.format(data[x,y][i]))[7]

#	print tmp

	tmp = [tmp[i:i+8] for i in range(0, len(tmp), 8)]
	dat  = []

	print "\n"

	for elem in tmp:
		sys.stdout.write((chr(int(elem,2)),'\0')[valid(chr(int(elem,2)))])

#	print "\n" + "-"*40

	print "\n"

	eom()


def saveImage(data, dimensions, fn):
	img = Image.new( 'RGB', (dimensions[0], dimensions[1]), "black")
	pixels = img.load() 

	for y in range(dimensions[1]):
		for x in range(dimensions[0]):
			pixels[x,y] = data[x,y]

	img.save(fn)

def information(data, dimensions):
	print (8*3)*(dimensions[1]+dimensions[0]), "bits of potential storage."
	print (3*(dimensions[1]+dimensions[0]))/8, "characters of potential storage."

def main():
	if len(sys.argv) < 2:
		print "usage: " + sys.argv[0] + " <encode/decode> <image_file> <if-encode-then-put-message-here>"
	else:
		if sys.argv[1].lower() == "encode" and len(sys.argv) == 4:
			inData, dimensions = openImage(sys.argv[2])
			message = str(sys.argv[3].strip("\r\n") + "`")
#			print message
			encoded = encodeData(inData, dimensions, message)
			fn = "out_"+clean(str(sys.argv[2])).strip("./")
			print fn
			saveImage(encoded, dimensions, fn)
		elif sys.argv[1].lower() == "decode" and len(sys.argv) == 3:
			inData, dimensions = openImage(sys.argv[2])
			decodeData(inData, dimensions)
		else:
			print "usage: " + sys.argv[0] + " <encode/decode> <image_file> <if-encode-then-put-message-here>"

if __name__ == "__main__":
    main()

#Encode example
	#inData, dimensions = openImage("test.png")
	#encoded = encodeData(inData, dimensions, "Ayylmao")
	#saveImage(encoded, dimensions, "out.png")


#Decode example
	#inData, dimensions = openImage("out.png")
	#decodeData(inData, dimensions)

#Check information example
	#inData, dimensions = openImage("test.png")
	#information(inData, dimensions)
