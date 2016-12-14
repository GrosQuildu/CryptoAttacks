#!/usr/bin/env python

import gmpy
import itertools

from Crypto.PublicKey import RSA

from Utils import *


class RSAKey(RSA._RSAobj):
    texts = []  # list of dict {'cipher':'ffaa', 'plain':'bb11'}
    identifier = ''


def generate(*args, **kwargs):
    tmp_key = RSA.generate(*args, **kwargs)
    tmp_key.__class__ = RSAKey
    tmp_key.identifier = id(tmp_key)
    return tmp_key


def construct(tup, identifier=''):
    """Construct key from tuple

    Args:
        tup(tuple):
               A tuple of long integers, with at least 2 and no
               more than 6 items. The items come in the following order:

               1. RSA modulus (n).
               2. Public exponent (e).
               3. Private exponent (d). Only required if the key is private.
               4. First factor of n (p). Optional.
               5. Second factor of n (q). Optional.
               6. CRT coefficient, (1/p) mod q (u). Optional
        identifier(string): unique identifier of key
    Returns:
        RSAKey
    """
    tmp_key = RSA.construct(tup)
    tmp_key.__class__ = RSAKey
    if identifier:
        tmp_key.identifier = identifier
    else:
        tmp_key.identifier = id(tmp_key)
    return tmp_key


def import_key(filename, *args, **kwargs):
    """Import key from file

    Args:
        filename(string): use it as key's id
    Returns:
        RSAKey
    """
    tmp_key = RSA.importKey(open(filename).read(), *args, **kwargs)
    tmp_key.__class__ = RSAKey
    tmp_key.identifier = filename
    return tmp_key


def common_prime(keys):
    """Find common prime in keys modules

    Args:
        keys(list): list of RSAKeys

    Returns:
        list: of RSAKeys for which factorization of n was found
    """
    priv_keys = []
    for pair in itertools.combinations(keys, 2):
        prime = gmpy.gcd(pair[0].n, pair[1].n)
        if prime != 1:
            log.info("Found common prime in: {}, {}".format(pair[0].identifier, pair[1].identifier))
            for x in xrange(2):
                d = long(gmpy.invert(pair[x].e, (prime - 1) * (pair[x].n/prime - 1)))
                priv_keys.append(construct((pair[x].n, pair[x].e, d), pair[x].identifier))
    return priv_keys


def wiener(key):
    n = key.n
    e = key.e
