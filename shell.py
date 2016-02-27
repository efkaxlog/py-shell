#!/usr/bin/env python3

import os

def isValid_command(command):
    if len(command) > 0:
        return command[0].isalnum()
    return False

while True:
    line = input('> ').split()
    
    if not isValid_command(line):
        continue

    pid = os.fork()
    if not pid:
        os.execvp(line[0], line)
    else:
        os.wait()

# 0. run this code and try `ls` to make sure that much works
# 1. handle arguments (`ls /`)
# 2. don't exit after a command runs (use os.fork and .wait)
# 3. I/O redirection (`echo hi > out`; use os.dup2)
# 4. builtins (`cd`, `pwd` for now)
# 5. forward signals (just SIGINT for now, use signal)
# 6. job control part 1: handle commands ending in `&`
# 7. job control part 2: Ctrl+Z == SIGSTOP, `jobs`, `fg`, `bg`
