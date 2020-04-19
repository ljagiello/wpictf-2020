# reversing - NotWannasigh

## Challenge
Please help! An evil script-kiddie (seriously, this is some bad code) was able
to get this ransomware "NotWannasigh" onto one of our computers. The program ran
and encrypted our file "flag.gif".

These are the resources we were able to gather for you:

NotWannasigh.zip - the malicious ransomware executable flag-gif.EnCiPhErEd - our
poor encrypted file that we need you to recover ransomNote.txt - the note left
behind by the ransomware. I'm not sure you'll find anything usefull here
192-168-1-11_potential-malware.pcap - a packet capture that our IDS isolated, it
seems that the program has some weird form of data exfiltration We need you to
reverse the malware and recover our flag.gif file. Good luck!

A note from the creator: Shoutout to Demonslay335 for challenge inspiration -
he's done some awesome work in fighting ransomware. Also, the ransomware in this
challenge is programmed to only target files named "flag.gif" so you shouldn't
need to worry about the accidental execution, I just zipped it out of habit/good
practice. Have fun and happy hacking!

Abjuri5t (John F.)
http://us-east-1.linodeobjects.com/wpictf-challenge-files/192-168-1-11_potential-malware.pcap

http://us-east-1.linodeobjects.com/wpictf-challenge-files/ransomNote.txt

http://us-east-1.linodeobjects.com/wpictf-challenge-files/flag-gif.EnCiPhErEd

http://us-east-1.linodeobjects.com/wpictf-challenge-files/NotWannasigh.zip

## Solution
Inside pcap we can find a single request:
```
ngrep -q -I 192-168-1-11_potential-malware.pcap -W byline
input: 192-168-1-11_potential-malware.pcap
filter: ((ip || ip6) || (vlan && (ip || ip6)))

T 192.168.1.11:39520 -> 108.61.127.136:80 [AP] #4
1585599106

T 108.61.127.136:80 -> 192.168.1.11:39520 [AP] #7
HTTP/1.1 400 Bad Request.
Server: nginx/1.16.1.
Date: Mon, 30 Mar 2020 20:14:58 GMT.
Content-Type: text/html.
Content-Length: 157.
Connection: close.
.
<html>.
<head><title>400 Bad Request</title></head>.
<body>.
<center><h1>400 Bad Request</h1></center>.
<hr><center>nginx/1.16.1</center>.
</body>.
</html>.
```
We can see string `1585599106` was transmitted and response was `HTTP 400`. If
we decompile the binary we can learn the string is a timestamp and it was used
to seed `srand()` function. Knowing seed value we can recreate the same values
for every `rand()` call.

The key used to encrypt file, got lenght of file and each byte was generated by
`rand()`:
```
  i = 0;
  while (i < (int)flag_file_size) {
    socket = rand(*(undefined *)(alStack240 + uVar4 * 0x1ffffffffffffffe));
    key[i] = (char)socket;
    i = i + 1;
  }
```
Because we know `timestamp`/`seed` we can recreate the key.

The only operation left is reverse original xor (run xor again):
```
  idx = 0;
  while( true ) {
    fd = orig_flag_fd;
    socket = fgetc(fd,*(undefined *)
                       (alStack240 + uVar4 * 0x1ffffffffffffffe + uVar5 * 0x1ffffffffffffffe));
    local_89 = (byte)socket;
    if ((int)flag_file_size <= idx) break;
    local_88[idx] = key[idx] ^ (byte)socket;
    idx = idx + 1;
  }
```

Decoder:
```python
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
```

## Flag
```
WPI{It_always_leets_a_little_weird_writing_malware}
```