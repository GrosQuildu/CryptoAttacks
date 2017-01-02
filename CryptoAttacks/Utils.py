#!/usr/bin/env python

import random
import string
import gmpy2
import math
from numbers import Number

# _ord = ord
# _chr = chr


# def ord(v):
#     if isinstance(v, int):
#         return v
#     elif isinstance(v, str):
#         return _ord(v)
#     else:
#         return _ord(v)


# def chr(v):
#     if isinstance(v, int):
#         return _chr(v)
#     elif isinstance(v, str):
#         return v
#     else:
#         return _chr(v)

class Log(object):
    def __init__(self):
        self._levels = {'debug': 30, 'info': 20, 'success': 10}
        self._level = self._levels['info']

    @property
    def level(self):
        return self._levels.keys()[self._levels.values().index(self._level)]

    @level.setter
    def level(self, value):
        if value not in self._levels.keys():
            print "Not in possible levels:", self._levels.keys()
        else:
            self._level = self._levels[value]

    def __call__(self, *args, **kwargs):
        print args

    def debug(self, a):
        min_level = 30
        if self._level >= min_level:
            print("[D]"+str(a))

    def info(self, a):
        min_level = 20
        if self._level >= min_level:
            print("[i]"+str(a))

    def success(self, a):
        min_level = 10
        if self._level >= min_level:
            print("[+]" + str(a))

    def error(self, a):
        min_level = 10
        if self._level >= min_level:
            print("[-]" + str(a))

    def critical_error(self, a):
        raise Exception(str(a))
log = Log()


def b2h(a):
    """Encode bytes to hex string"""
    return a.encode('hex')


def h2b(a):
    """Decode hex string to bytes"""
    a = a.strip()
    try:
        return a.decode('hex')
    except:
        return ('0'+a).decode('hex')


def h2i(a):
    """Decode hex string to int"""
    return int(a, 16)


def i2h(a):
    """Encode int as hex string"""
    return hex(a)[2:].strip('L')


def b2i(number_bytes, endian='big'):
    """Unpack bytes into int

    Args:
        number_bytes(int)
        endian(string): big/little

    Returns:
        int
    """
    if endian not in ['little', 'big']:
        log.critical_error("Bad endianness, must be big or little")

    if isinstance(number_bytes, Number):
        return int(number_bytes)

    if endian == 'little':
        number_bytes = number_bytes[::-1]
    return int(number_bytes.encode('hex'), 16)


def i2b(number, size=0, endian='big', signed=False):
    """Pack int to bytes

    Args:
        number(int)
        size(int): minimum size in bits, 0 if whatever it takes
        endian(string): big/little
        signed(bool): pack as two's complement if True (size must be given)

    Returns:
        string
    """
    if endian not in ['little', 'big']:
        log.critical_error("Bad endianness, must be big or little")

    if type(signed) != bool:
        log.critical_error("Bad sign, must be True or False")

    if size < 0:
        log.critical_error("Bad size, must be >= 0")

    if not size and signed:
        log.critical_error("Can't do signed packing without size")

    if number < 0 and not signed:
        log.critical_error("Negative number with signed==False")

    if not isinstance(number, Number):
        return number

    if signed and number < 0:
        number += (1 << size)

    number_bytes = ''
    while number:
        number_bytes += chr(number & 0xff)
        number >>= 8

    number_bytes += '\x00'*(int(math.ceil(size/8.0))-len(number_bytes))

    if endian == 'big':
        return number_bytes[::-1]
    return number_bytes


def is_printable(a, alphabet=string.printable, reliability=100.0):
    result = 0
    for char in a:
        if char in alphabet:
            result += 1
    if (result/float(len(a)))*100.0 >= reliability:
        return True
    return False


def xor_one(a, b):
    """Return a xor b as char"""
    if type(a) != int:
        a = ord(a)
    if type(b) != int:
        b = ord(b)
    return chr(a ^ b)


def xor(*args, **kwargs):
    """Xor given values

        args - strings to be xored
        expand - don't expand strings to size of the longest string if False
    Return xored strings
    """
    if 'expand' in kwargs and kwargs['expand'] is False:
        result = '\x00' * len(min(args, key=len))
    else:
        max_size = len(max(args, key=len))
        result = '\x00' * max_size
        args = [(arg * max_size)[:max_size] for arg in args]
    for one in args:
        result = [xor_one(x, y) for x, y in zip(one, result)]
    return ''.join(result)


def add_padding(data, block_size=16):
    """add PKCS#7 padding"""
    size = block_size - (len(data)%block_size)
    return data+chr(size)*size


def strip_padding(data, block_size=16):
    """strip PKCS#7 padding"""
    padding = ord(data[-1])
    if padding == 0 or padding > block_size or data[-padding:] != chr(padding)*padding:
        raise Exception("Invalid padding")
    return data[:-padding]


def hamming_distance(a, b):
    return sum(map(int, [bin(int(b2h(xor(x, y)), 16)).count('1') for x, y in zip(a, b)] ))


def chunks(data, block_size):
    return [data[0+i:block_size+i] for i in range(0, len(data), block_size)]


def print_chunks(data, delim=' | '):
    return delim.join([x.encode('hex') for x in data])


def random_str(length):
    return ''.join([string.printable[random.randint(0, len(string.printable)-1)] for x in xrange(length)])


def random_char():
    return chr(random.randint(32, 126))


def random_bytes(amount=1):
    return ''.join([chr(random.randint(0,255)) for x in xrange(amount)])


def random_prime(bytes=512):
    p = random.getrandbits(bytes)|1
    while not gmpy2.is_bpsw_prp(p):
        p = random.getrandbits(bytes)|1
    return p

