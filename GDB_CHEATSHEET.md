# gdb-cheatsheet

Get [gef](https://github.com/hugsy/gef) extension

## Run the program

- run: simply run the application

- start: set a breakpoint in main and run

- starti: stop execution at an elaboration phase

- b (breakpoint)

## Information

- i args

- i program

- i f (info frame), to analyze the stack

- i functions

- ...

## Disassemble

"disas" dumps machine code

## Resuming execution:

- c (continue)

- return

- j (jump)

- fin (finish), continue running until the selected function returns

- s (step)

- n (next)

- si (step assembly)

- ni (next assembly)

## Read the stack

- x/10x $esp


## Generate patterns
```
pattern create 128
> aaaabaaacaaadaaaeaaafaaagaa...
pattern search faaa
```
