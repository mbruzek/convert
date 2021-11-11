#!/usr/bin/env python3

"""
Convert strings to and from ASCII representation.

@copyright 2021 Matthew Bruzek

"""

import argparse


def ascii_to_binary(astring):
    """Convert an ASCII string to binary representation."""
    return ''.join(["{:08b}".format(ord(c)) for c in astring])


def ascii_to_hex(astring):
    """Convert an ASCII string to hexadecimal representation."""
    return '0x' + ''.join(["{:02X}".format(ord(c)) for c in astring])


def ascii_to_octal(astring):
    """Convert an ASCII string to ocal representation."""
    return '0o' + ''.join(["{:03o}".format(ord(c)) for c in astring])


def binary_to_ascii(bstring):
    """Convert a string with 1's and 0's to the ASCII representation."""
    return ''.join([chr(int(bstring[a:a+8], base=2)) for a in range(0, len(bstring), 8)])

def hex_to_ascii(xstring):
    """Convert a hexadecimal string to the ASCII representation."""
    if xstring.startswith('0x'):
        xstring = xstring[2:]
    return ''.join([chr(int(xstring[a:a+2], base=16)) for a in range(0, len(xstring), 2)])


def octal_to_ascii(ostring):
    """Convert an octal string to the ASCII representation."""
    if ostring.startswith('0o'):
        ostring = ostring[2:]
    return ''.join([chr(int(ostring[a:a+3], base=8)) for a in range(0, len(ostring), 3)])


def command_line():
    """Parse the arguements from the command line."""
    summary = 'Convert an ASCII string to binary, hex or octal and back.'
    parser = argparse.ArgumentParser(description=summary)
    parser.add_argument('-ab', '--ascii2binary', help='Convert ASCII to binary')
    parser.add_argument('-ao', '--ascii2octal', help='Convert ASCII to octal')
    parser.add_argument('-ax', '--ascii2hex', help='Convert ASCII to hex')
    parser.add_argument('-ba', '--binary2ascii', help='Convert binary to ASCII')
    parser.add_argument('-oa', '--octal2ascii', help='Convert octal to ASCII')
    parser.add_argument('-xa', '--hex2ascii', help='Convert hex to ASCII')
    arguments = parser.parse_args()

    if arguments.ascii2binary:
        print(ascii_to_binary(arguments.ascii2binary))
    if arguments.ascii2octal:
        print(ascii_to_octal(arguments.ascii2octal))
    if arguments.ascii2hex:
        print(ascii_to_hex(arguments.ascii2hex))
    if arguments.binary2ascii:
        print(binary_to_ascii(arguments.binary2ascii))
    if arguments.octal2ascii:
        print(octal_to_ascii(arguments.octal2ascii))
    if arguments.hex2ascii:
        print(hex_to_ascii(arguments.hex2ascii))


if __name__ == '__main__':
    command_line()
