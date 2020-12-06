import ctypes

#/bin/ls
shellcode = b"\x48\x31\xd2\x52\x48\xb8\x2f\x62"\
            b"\x69\x6e\x2f\x2f\x6c\x73\x50\x48"\
            b"\x89\xe7\x52\x57\x48\x89\xe6\x48"\
            b"\x8d\x42\x3b\x0f\x05"

libc = ctypes.CDLL('libc.so.6')
sc_ptr = ctypes.c_char_p(shellcode)

size = len(shellcode)
addr_aligned = ctypes.c_void_p(libc.valloc(size))
ctypes.memmove(addr_aligned, sc_ptr, size)
libc.mprotect(addr_aligned, size, 1 | 2 | 4) 

func = ctypes.cast(addr_aligned, ctypes.CFUNCTYPE(ctypes.c_void_p))
func()