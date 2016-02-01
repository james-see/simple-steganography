# simple-steganography
A simple python steganography tool. Make sure to install pillow via pip! Python 2.7.

# usage example

### to encode
<code>python (or python3) simple_steganography.py encode original.png "hello you!"</code>

### to decode
<code>python (or python3) simple_steganography.py decode out_original.png</code>

#Installing PIL (Python Imaging Library)
>> pip install Pillow

Any problems installing PIL?

sudo easy_install pillow
<br>
<br>
<br>
Mac:
Python 2.7
sudo pip install http://effbot.org/media/downloads/Imaging-1.1.7.tar.gz
<br>
or (easier)
Python 3.x
pip3 install pillow
<br><br>
Linux:
apt-get install python-dev;
apt-get install libjpeg-dev;
apt-get install libjpeg8-dev;
apt-get install libpng3 ;
apt-get install libfreetype6-dev;
ln -s /usr/lib/i386-linux-gnu/libfreetype.so /usr/lib;
ln -s /usr/lib/i386-linux-gnu/libjpeg.so /usr/lib;
ln -s /usr/lib/i386-linux-gnu/libz.so /usr/lib;
pip install PIL  --allow-unverified PIL --allow-all-external
<br><br>
Windows:
https://github.com/lightkeeper/lswindows-lib/blob/master/amd64/python/PIL-1.1.7.win-amd64-py2.7.exe?raw=true<br>
or<br>
get Pillow source from Pillow repository unpack and run
python setup.py install
