import sys, os, struct, binascii, ntpath
from PIL import Image

def clean(path):
	head, tail = ntpath.split(path)
	return tail or ntpath.basename(head)

def openImage(fn):
	inFile = Image.open(fn)
	pixels = inFile.load()
	return pixels, (inFile.size[0], inFile.size[1])

def eom():
	print "\nFinished.\n"
	exit(0)

def encodeData(data, dimensions, encode):

	encode_Data = []
	edit = data
	j = 0

	for char in encode:
		encode_Data.append('{:08b}'.format(ord(char)))
	encode_Data = ''.join(encode_Data)

	i = 0
	for y in range(dimensions[1]):
			for x in range(dimensions[0]):
				if i < len(encode_Data):
					i += 1

	if (dimensions[1] + dimensions[0])*3 > len(encode_Data) + 2:
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
		print "You can only store ", (dimensions[1]+dimensions[0])*3, "characters in this image!"
		eom()

def valid(input):
	if input in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=!@#$%^&*()_+~'\";:,./<>[]{}\\| \t\b\r":
		return False
	elif input == "`":
		eom()
	else:
		return True

def validByte(input):
	if input == "`":
		return True
	else:
		return False

def decodeData(data, dimensions):
	decode_Data = []
	tmp = ""
	dataFile = False

	for x in range(8):
		for i in range(3):
			tmp += str('{:08b}'.format(data[x,0][i]))[7]

	tmp = [tmp[i:i+8] for i in range(0, len(tmp), 8)]

	if chr(int(tmp[0],2)) == "`":
		dataFile = True

	tmp = ""

	if dataFile:

		print "Note: decoding data files is buggy and broken. It may never be fixed. Who knows."
		print "Please wait..."
		print "Reading pixels..."

		for y in range(dimensions[1]):
			for x in range(dimensions[0]):
					for i in range(3):
						tmp += str('{:08b}'.format(data[x,y][i]))[7]
		
		print "Decoding..."

		tmp = [tmp[i:i+8] for i in range(0, len(tmp), 8)]
		tmp = tmp[1:]
		dat = ""

		for elem in tmp:
			if not validByte(chr(int(elem,2))):
				dat += chr(int(elem,2))
			else:
				break
		
		print "Writing to file \"out.data\"..."

		open("out.data", "wb").write(bytes(dat[:-1]))

	else:
		print "Please wait..."
		print "Reading pixels..."

		for y in range(dimensions[1]):
			for x in range(dimensions[0]):
					for i in range(3):
						tmp += str('{:08b}'.format(data[x,y][i]))[7]

		print "Decoding..."
		print "\n"

		tmp = [tmp[i:i+8] for i in range(0, len(tmp), 8)]

		for elem in tmp:
			sys.stdout.write((chr(int(elem,2)),'\0')[valid(chr(int(elem,2)))])

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
	print (dimensions[1]+dimensions[0])*3, "characters of potential storage."

def main():
	if len(sys.argv) < 2:
		print "usage: " + sys.argv[0] + " <encode/decode> <image_file> <if-encode-then-put-message-here>"
	else:
		if sys.argv[1].lower() == "encode" and len(sys.argv) == 4:
			inData, dimensions = openImage(sys.argv[2])
			if os.path.isfile(sys.argv[3]):
				message = "`" + open(sys.argv[3],'rb').read() + "`"
			else:
				message = str(sys.argv[3].strip("\r\n") + "`")
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
