#!/usr/bin/python
from binascii import *
text = "010100t0z0t10zz11t00t0t0t00t10t00100t10111t0t00t00t001z0010000t1t0t00t00t00tt10010000110001101t1011t110110000t10010000001z001t00001100t0110110t1111011000010010"
text2 = text[::-1]
text3 = text2.replace("t","")
text4 = text3.replace("z","")
text_from_bits()
print text4
