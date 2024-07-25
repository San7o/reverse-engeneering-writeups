# ASSEMBLY

## Compare

```
cmpq source2, source1: it is like computing a-b without setting destination
testq source2, source1: it is like computing a&b without setting destination
```

## Jumps

```
Jump Type   Description
jmp 		Unconditional
je 			Equal/Zero
jne 		Not Equal/Not Zero
js 			Negative
jns 		Nonnegative
jg 			Greater
jge 		Greater or Equal
jl 			Less
jle 		Less or Equal
ja 			Above(unsigned)
jb 			Below(unsigned)

argc = lea ecx, dword [arg_4h]
argv = [exc + 4]
```

## scanf

```
0x0040080b      488d45b0       lea rax, qword [my_input]
0x0040080f      4889c6         mov rsi, rax
0x00400812      bf66094000     mov edi, 0x400966  ; "%s"
0x00400817      b800000000     mov eax, 0
0x0040081c      e89ffdffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
```

## strtok
```
in this case, splits the word on ".", each time it is called, it taks the next split

0x558fa8c0e877      488d45ee       leaq my_password, %rax
0x558fa8c0e87b      488d35450100.  leaq 0x558fa8c0e9c7, %rsi ; "."
0x558fa8c0e882      4889c7         movq %rax, %rdi
0x558fa8c0e885      e836feffff     callq sym.imp.strtok    ; char *strtok(char *s1, const char *s2)
0x558fa8c0e88a      488945b8       movq %rax, splitted_word
```

## strcmp
returns -1, 0, 1 of the lenght of the 2 string is respectively smaller. emal, larger

```
0x00400821      488d55d0       lea rdx, qword [string1]
0x00400825      488d45b0       lea rax, qword [string2]
0x00400829      4889d6         mov rsi, rdx
0x0040082c      4889c7         mov rdi, rax
0x0040082f      e8a2feffff     call sym.strcmp             ; int strcmp(const char *s1, const char *s2)
```

## strlen

```
0x558fa8c0e868      488d45ee       leaq my_password, %rax
0x558fa8c0e86c      4889c7         movq %rax, %rdi
0x558fa8c0e86f      e81cfeffff     callq sym.imp.strlen    ; size_t strlen(const char *s)
0x558fa8c0e874      8945b0         movl %eax, str_len
```

call a function

```
0x00400754 b    e821ffffff     call sym.compare_pwd
```


