from CryptoAttacks.Utils import *


def _left_rotate(val, r_bits, max_bits=32):
    return (val << r_bits % max_bits) & (2**max_bits-1) | \
           ((val & (2**max_bits-1)) >> (max_bits-(r_bits % max_bits)))


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
    p = '\x80' + '\x00' * 63
    p = p[:size]
    return data + p + i2b(len(data)*8, size=64, endian=endian)


def merkle_damgard(data, initial_state, compression_function):
    """Merkle-Damgard construction

    Args:
        data(string)
        initial_state(list of ints)
        compression_function(function)
    """
    state = initial_state[:]
    data_chunks = chunks(data, 64)
    log.debug("Start merkle-damgard, chunks are: {}".format(data_chunks))
    for chunk in data_chunks:
        log.debug("Process chunk: {} with state: {}".format(chunk.encode('hex'), state))
        state = compression_function(chunk, state)
    return state


def compression_function_sha1(chunk, state):
    """Sha1 compression function

    Args:
        chunk(string): len(chunk) == 64
        state(list of ints): len(state) == 5

    Returns:
        list of ints: compressed state
    """
    state = state[:]
    w = chunks(chunk, 4)
    w = map(b2i, w)
    for i in xrange(16, 80):
        w.append(_left_rotate(w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16], 1, 32))

    a = state[0]
    b = state[1]
    c = state[2]
    d = state[3]
    e = state[4]

    for i in range(80):
        if i // 20 == 0:
            f = d ^ (b & (c ^ d))
            k = 0x5A827999
        elif i // 20 == 1:
            f = b ^ c ^ d
            k = 0x6ED9EBA1
        elif i // 20 == 2:
            f = (b & c) | (b & d) | (c & d)
            k = 0x8F1BBCDC
        elif i // 20 == 3:
            f = b ^ c ^ d
            k = 0xCA62C1D6

        a, b, c, d, e = (_left_rotate(a, 5, 32) + f + e + k + w[i]) & 0xffffffff, a, _left_rotate(b, 30, 32), c, d

    state[0] = (state[0] + a) & 0xffffffff
    state[1] = (state[1] + b) & 0xffffffff
    state[2] = (state[2] + c) & 0xffffffff
    state[3] = (state[3] + d) & 0xffffffff
    state[4] = (state[4] + e) & 0xffffffff
    return state


def sha1(data, initial_state=[0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0], padding=None):
    """Compute SHA1

    Args:
        data(string)
        initial_state(list of ints)
        padding(string/None): if None, padding will be computed

    Returns:
        digest(string)
    """
    if not padding:
        data = add_md_padding(data, endian='big')
    else:
        data += padding
    final_state = merkle_damgard(data, initial_state, compression_function_sha1)
    return ''.join(map(lambda x: i2b(x, size=32), final_state))


def compression_function_md4(chunk, state):
    """MD4 compression function, taken from: https://gist.github.com/tristanwietsma/5937448

    Args:
        chunk(string): len(chunk) == 64
        state(list of ints): len(state) == 4

    Returns:
        list of ints: compressed state
    """
    def _f(x, y, z): return x & y | ~x & z

    def _g(x, y, z): return x & y | x & z | y & z

    def _h(x, y, z): return x ^ y ^ z

    def _f1(a, b, c, d, k, s, X): return _left_rotate(a + _f(b, c, d) + X[k], s)

    def _f2(a, b, c, d, k, s, X): return _left_rotate(a + _g(b, c, d) + X[k] + 0x5a827999, s)

    def _f3(a, b, c, d, k, s, X): return _left_rotate(a + _h(b, c, d) + X[k] + 0x6ed9eba1, s)

    state = state[:]
    x = chunks(chunk, 4)
    x = map(lambda one_x: b2i(one_x, endian='little'), x)
    a, b, c, d = state

    a = _f1(a, b, c, d, 0, 3, x)
    d = _f1(d, a, b, c, 1, 7, x)
    c = _f1(c, d, a, b, 2, 11, x)
    b = _f1(b, c, d, a, 3, 19, x)
    a = _f1(a, b, c, d, 4, 3, x)
    d = _f1(d, a, b, c, 5, 7, x)
    c = _f1(c, d, a, b, 6, 11, x)
    b = _f1(b, c, d, a, 7, 19, x)
    a = _f1(a, b, c, d, 8, 3, x)
    d = _f1(d, a, b, c, 9, 7, x)
    c = _f1(c, d, a, b, 10, 11, x)
    b = _f1(b, c, d, a, 11, 19, x)
    a = _f1(a, b, c, d, 12, 3, x)
    d = _f1(d, a, b, c, 13, 7, x)
    c = _f1(c, d, a, b, 14, 11, x)
    b = _f1(b, c, d, a, 15, 19, x)

    a = _f2(a, b, c, d, 0, 3, x)
    d = _f2(d, a, b, c, 4, 5, x)
    c = _f2(c, d, a, b, 8, 9, x)
    b = _f2(b, c, d, a, 12, 13, x)
    a = _f2(a, b, c, d, 1, 3, x)
    d = _f2(d, a, b, c, 5, 5, x)
    c = _f2(c, d, a, b, 9, 9, x)
    b = _f2(b, c, d, a, 13, 13, x)
    a = _f2(a, b, c, d, 2, 3, x)
    d = _f2(d, a, b, c, 6, 5, x)
    c = _f2(c, d, a, b, 10, 9, x)
    b = _f2(b, c, d, a, 14, 13, x)
    a = _f2(a, b, c, d, 3, 3, x)
    d = _f2(d, a, b, c, 7, 5, x)
    c = _f2(c, d, a, b, 11, 9, x)
    b = _f2(b, c, d, a, 15, 13, x)

    a = _f3(a, b, c, d, 0, 3, x)
    d = _f3(d, a, b, c, 8, 9, x)
    c = _f3(c, d, a, b, 4, 11, x)
    b = _f3(b, c, d, a, 12, 15, x)
    a = _f3(a, b, c, d, 2, 3, x)
    d = _f3(d, a, b, c, 10, 9, x)
    c = _f3(c, d, a, b, 6, 11, x)
    b = _f3(b, c, d, a, 14, 15, x)
    a = _f3(a, b, c, d, 1, 3, x)
    d = _f3(d, a, b, c, 9, 9, x)
    c = _f3(c, d, a, b, 5, 11, x)
    b = _f3(b, c, d, a, 13, 15, x)
    a = _f3(a, b, c, d, 3, 3, x)
    d = _f3(d, a, b, c, 11, 9, x)
    c = _f3(c, d, a, b, 7, 11, x)
    b = _f3(b, c, d, a, 15, 15, x)

    state[0] = (state[0] + a) & 0xffffffff
    state[1] = (state[1] + b) & 0xffffffff
    state[2] = (state[2] + c) & 0xffffffff
    state[3] = (state[3] + d) & 0xffffffff
    return state


def md4(data, initial_state=[0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476], padding=None):
    """Compute MD4

    Args:
        data(string)
        initial_state(list of ints)
        padding(string/None): if None, padding will be computed

    Returns:
        digest(string)
    """
    if not padding:
        data = add_md_padding(data, endian='little')
    else:
        data += padding
    final_state = merkle_damgard(data, initial_state, compression_function_md4)
    return ''.join(map(lambda x: i2b(x, size=32, endian='little'), final_state))


def length_extension(hash, new_message, size=None, type='sha1'):
    implemented_functions = ['sha1', 'md4']
    if type not in implemented_functions:
        log.critical_error("{} not implemented, type must be one of {}".format(type, implemented_functions))

    if type == 'sha1':
        endian = 'big'
        hash_function = sha1
    elif type == 'md4':
        endian = 'little'
        hash_function = md4

    old_padding = add_md_padding('a' * size, endian=endian)[size:]
    new_data_size = len(new_message)+len(old_padding)+size
    new_padding = add_md_padding('a'*new_data_size, endian=endian)[new_data_size:]
    h = map(lambda x: b2i(x, endian=endian), chunks(hash, 4))
    return hash_function(new_message, h, new_padding), old_padding+new_message
