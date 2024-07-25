# radare 2 framework

Commands:

| Command                        | Description                                                 |
| ------------------------------ | ----------------------------------------------------------- |
| @                              | at                                                          |
| r2 -d <\ELF> <\args>           | Open r2                                                     |
| ?                              | Help                                                        |
| aaa                            | Start analyzing                                             |
| iS                             | Show sections                                               |
| afl                            | List functions                                              |
| s sym.main                     | Seek to function                                            |
| pdf @main                      | Show main assembly                                          |
| db <\memory>                   | Set breakpoint                                              |
| dc                             | Start execution                                             |
| dr                             | View register values (blue = pointer, green = value stored) |
| px @rbp-0x4                    | Show the hex value of the variable                          |
| ds                             | Move to next instruction                                    |
| afvn \[new_name] (\[old_name]) | Change variable name                                        |
| <\offset>                      | Go to that offset (e.g., 0x558fa8c0e9c7)                    |
| V                              | Visual mode (USE ONLY KEYBOARD!!!) (arrows are cool)        |
| v                              | Select function                                             |
| c                              | Show cursor                                                 |
| space                          | Graph mode                                                  |
| VV                             | Graph mode (USE ONLY KEYBOARD!!!)                           |
| p                              | Change graph type                                           |
| tab                            | Select next block                                           |
| c                              | Move block                                                  |
| ood                            | Restart                                                     |


### Example command flow

```bash
# open a file
radare2 ./file
# analyze a file
aaa
# list functions
afl
# enter a function
pdf @<function name>
# set breakpoint
db <memory address>
# start executioin, waybe ood is necessary
dc

```
## Use UTF-8 to show cool arrows
e scr.utf8 = true

## Types of syntax
e asm.syntax=att
e asm.syntax=intel

\[var] indivates the memory index whose valuse is var

Many starting instructions can be ignored

Hex values, when tranformed into integers, van be negative. Just look at the first bit in binary
