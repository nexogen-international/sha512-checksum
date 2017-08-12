#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
NEXOGEN - Calculate SHA-512 from input stream
"""

#
# Copyright (c) 2017 NEXOGEN
# Author: Mark Farkas <mark.farkas@nexogen.hu>
#

# Usage:
# From command prompt, type the following command without quotation marks:
# Windows: "type <filename> | python nexogen_sha512_checksum.py"
# Linux:   "cat <filename> | python nexogen_sha512_checksum.py"
# where <filename> is the full path of the file

import hashlib
import sys

def calculate_sha512_hexdigest(byte_array):
    """
    Calculate SHA-512 hexadecimal digest from byte array
    """
    hash_algorithm = hashlib.sha512()
    hash_algorithm.update(byte_array)
    hex_digest = hash_algorithm.hexdigest()
    return hex_digest

def read_bytes_from_stdin_to_eof():
    """
    Read all bytes from STDIN to EOF
    """
    is_python3 = sys.version_info >= (3, 0)
    if is_python3:
        source = sys.stdin.buffer
    else:
        # Python 2 on Windows opens sys.stdin in text mode, and
        # binary data that read from it becomes corrupted on \r\n
        if sys.platform == "win32":
            # set sys.stdin to binary mode
            import os
            import msvcrt
            msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)
        source = sys.stdin
    byte_array = source.read()
    return byte_array

def main():
    """
    Main method.
    """
    byte_array = read_bytes_from_stdin_to_eof()
    hex_digest = calculate_sha512_hexdigest(byte_array)
    print(hex_digest)

if __name__ == '__main__':
    main()
