#!/usr/bin/python3
import decompile

ownDir = dir(decompile)
if __name__ == '__main__':
    filtered_dir = [name for name in ownDir if not name.startswith('__')]
    for i in range(len(filtered_dir)):
        print(filtered_dir[i])
