#!/usr/bin/env python
from ctypes import *

TIMESTAMP = 1585599106
ENC_FILENAME = "flag-gif.EnCiPhErEd"
DEC_FILENAME = "flag.gif"

libc = CDLL("libc.so.6")

libc.srand(TIMESTAMP)

byte_list = []
with open(ENC_FILENAME) as f:
    while True:
        byte = f.read(1)
        if not byte:
            break
        rand = libc.rand() & 0xFF
        decoded_byte = int(rand) ^ ord(byte)
        byte_list.append(decoded_byte)

f = open(DEC_FILENAME, 'w+b')
binary_format = bytearray(byte_list)
f.write(binary_format)
f.close()


"""
WPI{It_always_feels_a_little_weird_writing_malware}