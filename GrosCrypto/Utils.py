#!/usr/bin/env python

import random
import string
import gmpy2

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
        raise Exception("[-]" + str(a))
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


def b2i(a):
    """Decode bytes to int"""
    return int(a.encode('hex'), 16)


def i2b(a):
    """Encode int to bytes"""
    a = hex(a)[2:].strip('L')
    return ('0'*(len(a) & 1) + a).decode('hex')


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
    size = block_size - (len(data)%block_size)
    return data+chr(size)*size


def hamming_distance(a, b):
    return sum(map(int, [bin(int(b2h(xor(x, y)), 16)).count('1') for x, y in zip(a, b)] ))


def chunks(data, length):
    return [data[0+i:length+i] for i in range(0, len(data), length)]


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

