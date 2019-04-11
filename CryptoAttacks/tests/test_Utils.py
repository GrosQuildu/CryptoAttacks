#!/usr/bin/env python

from __future__ import absolute_import, division, print_function

import hashlib
import random
from builtins import bytes, range

from CryptoAttacks.Utils import h2b, log, random_bytes


def test_xor():
    assert xor("A", "A") == b"\x00"
    assert xor(b"A", "A") == b"\x00"
    assert xor(b"A", b"A") == b"\x00"
    assert xor("A", "A", b"A") == b"A"


def test_add_padding():
    assert add_padding('asd') == b'asd\r\r\r\r\r\r\r\r\r\r\r\r\r'
    assert add_padding(b'asd') == b'asd\r\r\r\r\r\r\r\r\r\r\r\r\r'
    assert add_padding('asd', 10) == b'asd\x07\x07\x07\x07\x07\x07\x07'
    assert add_padding(b'asd', 10) == b'asd\x07\x07\x07\x07\x07\x07\x07'
    assert strip_padding(add_padding(b'asd', 10)) == b'asd'


def run():
    log.level = 'info'
    test_xor()
    test_add_padding()

if __name__ == "__main__":
    run()
