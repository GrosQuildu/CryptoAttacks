from __future__ import absolute_import, division, print_function

import hashlib
import math
import random
import string
from binascii import hexlify
from builtins import bytes, chr, map, range, str, zip
from numbers import Number

import gmpy2
import requests
from bs4 import BeautifulSoup

from termcolor import colored


class Log(object):
    def __init__(self):
        self._levels = {'debug': 30, 'info': 20, 'success': 10}
        self._level = self._levels['info']

    @property
    def level(self):
        return list(self._levels.keys())[list(self._levels.values()).index(self._level)]

    @level.setter
    def level(self, value):
        if value not in list(self._levels.keys()):
            print("Not in possible levels:", list(self._levels.keys()))
        else:
            self._level = self._levels[value]

    def __call__(self, *args, **kwargs):
        print(args)

    def debug(self, a):
        min_level = 30
        if self._level >= min_level:
            print("[{}] ".format(colored('D', 'magenta')) + str(a))

    def info(self, a):
        min_level = 20
        if self._level >= min_level:
            print("[{}] ".format(colored('i', 'yellow', attrs=['bold'])) + str(a))

    def success(self, a):
        min_level = 10
        if self._level >= min_level:
            print("[{}] ".format(colored('+', 'green', attrs=['bold'])) + str(a))

    def error(self, a):
        min_level = 10
        if self._level >= min_level:
            print("[{}] ".format(colored('i', 'red', attrs=['bold'])) + str(a))

    def critical_error(self, a):
        raise Exception(str(a))

log = Log()


def b2h(a, size=0):
    """Encode bytes to hex string"""
    return hexlify(a).decode()


def h2b(a):
    """Decode hex string to bytes"""
    a = a.strip()
    try:
        return bytes.fromhex(a)
    except (TypeError, ValueError):
        try:
            return bytes.fromhex(bytes(b'0')+a)
        except Exception as e:
            print(e, a)


def h2i(a):
    """Decode hex string to int"""
    return int(a, 16)


def i2h(a, size=0):
    """Encode int as hex string"""
    return hexlify(i2b(a, size=size)).decode()


def b2i(number_bytes, endian='big'):
    """Unpack bytes into int

    Args:
        number_bytes(bytes)
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
    return int(hexlify(number_bytes).decode(), 16)


def i2b(number, size=0, endian='big', signed=False):
    """Pack int to bytes

    Args:
        number(int)
        size(int): minimum size in bits, 0 if whatever it takes
        endian(string): big/little
        signed(bool): pack as two's complement if True (size must be given)

    Returns:
        bytes
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

    number_bytes = bytes(b'')
    while number:
        number_bytes += bytes([number & 0xff])
        number >>= 8

    number_bytes += bytes(b'\x00'*(int(math.ceil(size/8.0))-len(number_bytes)))

    if endian == 'big':
        return number_bytes[::-1]
    return number_bytes


def is_printable(a, alphabet=string.printable, reliability=100.0):
    result = 0
    for char in a:
        if char in alphabet:
            result += 1
    if (result / len(a))*100.0 >= reliability:
        return True
    return False


def xor(*args, **kwargs):
    """Xor given values

    Args:
        args - bytes to be xored
        expand(bool) - don't expand bytes to size of the longest string if False

    Return:
        xored bytes
    """
    if 'expand' in kwargs and kwargs['expand'] is False:
        result = bytes(len(min(args, key=len)))
    else:
        max_size = len(max(args, key=len))
        result = bytes(max_size)

    for one in args:
        one = bytes(one)
        result = bytes([result[x] ^ one[x % len(one)] for x in range(len(result))])
    return result


def add_padding(data, block_size=16):
    """add PKCS#7 padding"""
    size = block_size - (len(data) % block_size)
    return data + bytes([size]*size)


def strip_padding(data, block_size=16):
    """strip PKCS#7 padding"""
    padding = int(data[-1])
    if padding == 0 or padding > block_size or data[-padding:] != bytes([padding]*padding):
        raise Exception("Invalid padding")
    return data[:-padding]


def add_rsa_signature_padding(data, size=1024, hash_function='sha1'):
    """add PKCS#1 v1.5 sign padding"""
    hash_asn1 = {
        'md5': b'\x30\x20\x30\x0c\x06\x08\x2a\x86\x48\x86\xf7\x0d\x02\x05\x05\x00\x04\x10',
        'sha1': b'\x30\x21\x30\x09\x06\x05\x2b\x0e\x03\x02\x1a\x05\x00\x04\x14',
        'sha256': b'\x30\x31\x30\x0d\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x01\x05\x00\x04\x20',
        'sha384': b'\x30\x41\x30\x0d\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x02\x05\x00\x04\x30',
        'sha512': b'\x30\x51\x30\x0d\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x03\x05\x00\x04\x40'
    }
    if hash_function not in list(hash_asn1.keys()):
        log.critical_error("Hash function {} not supported".format(hash_function))

    hash_data = getattr(hashlib, hash_function)(data).digest()
    padded = hash_asn1[hash_function] + hash_data
    padded = bytes(b'\xff'*(size//8 - len(padded) - 2))
    padded = bytes(b'\x00\x01') + padded
    return padded + data


def add_md_padding(data, endian='big'):
    """Merkle-Damgard padding

    Args: data(string)
    Returns: data+padding(string)
    """
    size = len(data) & 0x3f  # len_in_bytes % 64
    if size < 56:
        size = 56 - size
    else:
        size = 120 - size
    p = bytes(b'\x80') + bytes(b'\x00'*63)
    p = p[:size]
    return data + p + i2b(len(data)*8, size=64, endian=endian)


def hamming_distance(a, b):
    return sum(map(int, [bin(int(b2h(xor(x, y)), 16)).count('1') for x, y in zip(a, b)] ))


def chunks(data, block_size):
    """Split data to list of chunks"""
    return [data[0+i:block_size+i] for i in range(0, len(data), block_size)]


def print_chunks(data, delim=' | '):
    return delim.join([b2h(x) for x in data])


def random_bytes_alpha(length):
    alphabet = string.printable[:-5]
    return bytes(b''.join([alphabet[random.randint(0, len(alphabet )-1)].encode() for x in range(length)]))


def random_char():
    return chr(random.randint(32, 126))


def random_bytes(amount=1):
    return bytes([random.randint(0,255) for x in range(amount)])


def random_prime(bytes=512):
    p = random.getrandbits(bytes)|1
    while not gmpy2.is_bpsw_prp(p):
        p = random.getrandbits(bytes)|1
    return p


def power_of_two(number):
    """number == (2^x)*b, returns x"""
    return len(bin(number)) - len(bin(number).rstrip('0'))


def factordb(number):
    """Ask factordb.com for factorization

    Args:
        number(int)
    Returns:
        status(string):
                        C - Composite, no factors known
                        CF - Composite, factors known
                        FF - Composite, fully factored
                        P - Definitely prime
                        Prp - Probably prime
                        U - Unknown
                        Unit - Just for 1
                        N - This number is not in database (and was not added due to your settings)
                        * - Added to database during this request
        digits(int)
        factors(dict): {factor: power,...}
    """
    def get_by_id(id):
        resp = requests.get(url, params={'id': id})
        dom = BeautifulSoup(resp.text)
        return int(dom.find('form').find('input', {'name':'query'})['value'])

    url = 'http://factordb.com/index.php'
    resp = requests.get(url, params={'query': number})
    dom = BeautifulSoup(resp.text, features="html.parser")
    results = dom.findAll('table')[1].findAll('tr')[2]

    status = results.findAll('td')[0].text
    digits = results.findAll('td')[1].text
    digits = int(digits[:digits.index('(')])

    factors_txt = results.findAll('td')[2].findAll('a')
    factors_txt = factors_txt[1:]
    factors = {}
    for factor_id in range(len(factors_txt)):
        if '...' in factors_txt[factor_id].getText():
            tmp = factors_txt[factor_id]['href']
            id = tmp[tmp.rindex('id=')+3:]
            factors[get_by_id(id)] = 1
        else:
            to_parse = factors_txt[factor_id].text
            if '^' in to_parse:
                a, b = list(map(int, to_parse.split('^')))
                factors[a] = b
            else:
                factors[int(to_parse)] = 1
    return status, digits, factors
