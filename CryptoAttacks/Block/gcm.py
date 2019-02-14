from __future__ import absolute_import, division, print_function

from builtins import bytes, range, int
import math
from itertools import combinations
try:
    from itertools import zip_longest
except:
    from itertools import izip_longest as zip_longest
from random import randint
from copy import deepcopy

from Crypto.Cipher import AES

from CryptoAttacks.Utils import random_bytes, xor, i2b, b2i, b2h, log
from CryptoAttacks.Math import egcd, invmod


def deg(n):
    """Find degree of polynomial
    
    Args:
        n(Polynomial_128/list/int)
    
    Returns:
        int
    """
    if isinstance(n, Polynomial_128):
        n = n.coefficients
    if type(n) == list:
        for d in reversed(range(len(n))):
            if n[d].to_int() != 0:
                return d
        return -1
    else:
        if n == 0:
            return -1
        return int(math.floor(math.log(n, 2) + 1))


class Polynomial_2():
    """Polynomial with coefficients in GF(2)"""

    def __init__(self, coefficients):
        """x^3 + x + 1  == 0b1101 == [3, 1, 0]"""
        self.coefficients = Polynomial_2.convert_coefficients(coefficients)

    @staticmethod
    def convert_coefficients(coefficients):
        if type(coefficients) == list:
            coefficients = Polynomial_2.list_to_int(coefficients)
        elif type(coefficients) == bytes:
            # reverse bit order
            coefficients = int(''.join(map(lambda x: '{:08b}'.format(x), coefficients))[::-1], 2)
        elif isinstance(coefficients, int):
            pass
        else:
            raise ValueError("Bad coefficients: {} ({})".format(coefficients, type(coefficients)))
        return coefficients


    @staticmethod
    def egcd(a, b):
        """Extended Euclidean algorithm"""
        a, b = map(Polynomial_2, [a, b])
        s0, t0, s1, t1 = map(Polynomial_2, [1, 0, 0, 1])
        while b.coefficients:
            q, a, b = a/b, b, a%b
            s0, s1 = s1, s0 - q*s1
            t0, t1 = t1, t0 - q*t1
        return a, s0, t0

    @staticmethod
    def list_to_int(coefficients):
        result = 0
        for coef in coefficients:
            result |= 1<<coef
        return result


    def __str__(self):
        return self.to_poly()


    def __getitem__(self, no):
        if not isinstance(no, int):
            return 'No must be a number'
        if no < 0 or no > self.to_bits():
            return 'Bad no'
        return int(self.to_bits()[no])


    def to_bits(self):
        return '{:b}'.format(self.coefficients)[::-1]


    def to_int(self):
        return self.coefficients


    def to_poly(self):
        if self.coefficients == 0:
            return '0'
        result = ''
        for i, coef in enumerate(self.to_bits()):
            if coef == '1':
                result = 'x^{} + '.format(i) + result
        return result[:-3]


    def to_list(self):
        return list(map(int, list(self.to_bits())))


    def __add__(self, other):
        return Polynomial_2(self.coefficients ^ other.coefficients)


    def __sub__(self, other):
        return self + other


    def __mul__(self, other):
        if isinstance(other, int):
            other = Polynomial_2(other)

        p = 0
        a = self.coefficients
        b = other.coefficients

        while a > 0:
            if a & 1:
                p = p ^ b
            a = a >> 1
            b = b << 1

        return Polynomial_2(p)


    def __rmul__(self, other):
        return self.__mul__(other)


    def __divmod__(self, other):
        a = self.coefficients
        b = other.coefficients
        q, r = 0, a

        while deg(r) >= deg(b):
            d = deg(r) - deg(b)
            q = q ^ (1 << d)
            r = r ^ (b << d)

        return Polynomial_2(q), Polynomial_2(r)

    def __mod__(self, other):
        return self.__divmod__(other)[1]


    def __div__(self, other):
        return self.__divmod__(other)[0]

    def __floordiv__(self, other):
        return self.__div__(other)

    def __truediv__(self, other):
        return self.__div__(other)


    def __pow__(self, y):
        p = Polynomial_2(1)
        b = Polynomial_2(self.coefficients)

        while y > 0:
            if y & 1:
                p *= b
            y >>= 1
            b *= b
        return p


    def __eq__(self, other):
        return self.coefficients == other.coefficients


    def __hash__(self):
        return hash(self.to_int())


class GF_2k():
    """GF(2^k) with elements represented as polynomials with coefficients in GF(2)"""

    def __init__(self, coefficients, k, modulus):
        """x^3 + x + 1  == 0b1101"""
        self.coefficients = Polynomial_2.convert_coefficients(coefficients)
        self.k = k

        if isinstance(modulus, Polynomial_2):
            self.modulus = modulus
        else:
            self.modulus = Polynomial_2(modulus)

        tmp = Polynomial_2(self.coefficients) % self.modulus
        self.coefficients = tmp.coefficients


    def __str__(self):
        return self.to_poly()


    def __repr__(self):
        return self.__str__()


    def __getitem__(self, no):
        if not isinstance(no, int):
            return 'No must be a number'
        if no > self.to_bits():
            return 'Bad no'
        return int(self.to_bits()[no])


    def to_bytes(self):
        return bytes(i2b(int(self.to_bits(), 2)).rjust(self.k//8, bytes(b'\x00')))


    def to_bits(self):
        return '{:b}'.format(self.coefficients).zfill(self.k)[::-1]


    def to_int(self):
        return self.coefficients


    def to_poly(self):
        if self.coefficients == 0:
            return '0'
        result = ''
        for i, coef in enumerate(self.to_bits()):
            if coef == '1':
                result = 'x^{} + '.format(i) + result
        return result[:-3]


    def to_list(self):
        return list(map(int, list(self.to_bits())))


    def __add__(self, other):
        return GF_2k(self.coefficients ^ other.coefficients, self.k, self.modulus)


    def __sub__(self, other):
        return self + other


    def __mul__(self, other):
        if isinstance(other, int):
            other = GF_2k(other, self.k, self.modulus)

        p = 0
        a = self.coefficients
        b = other.coefficients
        m = self.modulus.coefficients

        while a > 0:
            if a & 1:
                p = p ^ b
            a = a >> 1
            b = b << 1

            if deg(b) == deg(m):
                b = b ^ m

        return GF_2k(p, self.k, self.modulus)


    def invmod(self):
        """Modular inverse. a*invmod(a) == 1 (mod n)"""
        d, s, t = Polynomial_2.egcd(self.coefficients, self.modulus.coefficients)
        if d.coefficients != 1:
            raise ValueError("Modular inverse doesn't exists ({}**(-1) % {})".format(self, self.modulus))
        return GF_2k(s.coefficients, self.k, self.modulus)


    def __mod__(self, other):
        log.error('Modulo not allowed')
        return None
        # result = Polynomial_2(self.coefficients) % Polynomial_2(other.coefficients)
        # return GF_2k(result.coefficients, self.k, self.modulus)


    def __div__(self, other):
        return self * other.invmod()

    def __floordiv__(self, other):
        return self.__div__(other)
        
    def __truediv__(self, other):
        return self.__div__(other)


    def __pow__(self, y):
        p = GF_2k(1, self.k, self.modulus)
        b = GF_2k(self.coefficients, self.k, self.modulus)

        while y > 0:
            if y & 1:
                p *= b
            y >>= 1
            b *= b
        return p


    def __eq__(self, other):
        return self.k == other.k and self.coefficients == other.coefficients


    def __hash__(self):
        return hash(self.to_bytes() + bytes(b'-') + bytes(self.k))

    
class GF_2k_generator():
    """Helper for generating GF(2^k) with given k and modulus"""

    def __init__(self, k, modulus):
        self.k = k
        self.modulus = modulus

    def __call__(self, coefficients):
        return GF_2k(coefficients, self.k, self.modulus)


class Polynomial_128():
    """Polynomial with coefficients in GF(2^128)"""

    def __init__(self, coefficients):
        """12*x^2 + x + 43 == [GF_2k(43,128,m), GF_2k(1,128,m), GF_2k(12,128,m)]"""
        self.coefficients = coefficients
        self.k = self.coefficients[0].k
        self.modulus = self.coefficients[0].modulus

        for no in range(len(self.coefficients)):
            if self.coefficients[no].k != self.k:
                raise ValueError("Coefficients not consistient: k=={}, coef[{}].k=={}".format(self.k, no, self.coefficients[no].k))
            if self.coefficients[no].modulus.coefficients != self.modulus.coefficients:
                raise ValueError("Coefficients not consistient: modulus=={}, coef[{}].modulus=={}".format(self.modulus, no, self.coefficients[no].modulus))


    def __add__(self, other):
        return Polynomial_128(
            [a+b for a,b in zip_longest(self.coefficients, other.coefficients,
                fillvalue=GF_2k(0,self.k,self.modulus))])


    def __sub__(self, other):
        return self + other


    def __str__(self):
        if len(self.coefficients) == 0 or deg(self) < 0:
            return '0'
        result = ''
        for i, coef in enumerate(self.coefficients):
            if coef.to_int() != 0:
                if coef.to_int() == 1:
                    result = 'x^{} + '.format(i) + result
                else:
                    result = '{}*x^{} + '.format(coef.to_int(), i) + result
        return result[:-3]


    def __repr__(self):
        return self.__str__()


    def __mul__(self, other):
        if isinstance(other, GF_2k):
            other = Polynomial_128([other])

        if self.is_zero() or other.is_zero():
            return self.zero_element()

        k = deg(self) + 1
        l = deg(other) + 1
        c = [GF_2k(0,self.k,self.modulus)]*(k+l-1)
        for i in range(k):
            for j in range(l):
                c[i+j] += self.coefficients[i]*other.coefficients[j]
        return Polynomial_128(c)


    def __divmod__(self, other):
        k = deg(self) + 1
        l = deg(other) + 1

        if k < l:
            return Polynomial_128([GF_2k(0,self.k,self.modulus)]), self

        t = other.coefficients[l-1].invmod()
        r = [a for a in self.coefficients]
        q = [GF_2k(0,self.k,self.modulus)]*(k-l+1)
        for i in reversed(range(k-l+1)):
            q[i] = t*r[i+l-1]
            for j in range(l):
                r[i+j] -= q[i]*other.coefficients[j]
        return Polynomial_128(q), Polynomial_128(r)
        

    def __mod__(self, other):
        return self.__divmod__(other)[1]


    def __div__(self, other):
        if isinstance(other, GF_2k):
            return self.__divmod__(Polynomial_128([other]))[0]
        else:
            return self.__divmod__(other)[0]

    def __floordiv__(self, other):
        return self.__div__(other)
        
    def __truediv__(self, other):
        return self.__div__(other)


    def __pow__(self, y):
        p = self.one_element()
        b = Polynomial_128(self.coefficients)

        while y > 0:
            if y & 1:
                p *= b
            y >>= 1
            b *= b
        return p


    def powmod(self, y, m):
        p = self.one_element()
        b = Polynomial_128(self.coefficients) % m

        while y > 0:
            if y & 1:
                p = (p*b) % m
            y >>= 1
            b = (b*b) % m
        return p


    def __eq__(self, other):
        return self.k == other.k and self.modulus == other.modulus and\
                  all([a == b for a,b in zip(self.coefficients, other.coefficients)])


    def __hash__(self):
        return hash(''.join(map(str,map(hash, self.coefficients))))

    def is_zero(self):
        return len(self.coefficients) == 0 or deg(self) < 0

    def is_one(self):
        return deg(self) == 0 and self.coefficients[0].to_int() == 1

    def zero_element(self):
        """0*x^0"""
        return Polynomial_128([GF_2k(0,self.k,self.modulus)])

    def one_element(self):
        """1*x^0"""
        return Polynomial_128([GF_2k(1,self.k,self.modulus)])

    def element(self):
        """x^1"""
        return Polynomial_128([GF_2k(0,self.k,self.modulus), GF_2k(1,self.k,self.modulus)])

    def monic(self):
        f = deepcopy(self)
        if self.coefficients[deg(f)].to_int() != 1:
            f /= self.coefficients[deg(f)]
        return f


aes_polynomial = GF_2k_generator(128, [128, 7, 2, 1, 0])


def encrypt_ctr(plaintext, key, nonce, block_size=16, initial_value=0):
    aes = AES.new(key, AES.MODE_ECB)
    key_stream = bytes(b'')
    for counter in range(int(math.ceil(len(plaintext)/16.))):
        key_stream += bytes(aes.encrypt(nonce + i2b(counter+initial_value, size=8*(block_size-len(nonce)), endian='big')))
    return xor(plaintext, key_stream)


def aes_bytes_to_poly_blocks(ciphertext, additional, block_size=16):
    """Convert ciphertext to list of GF(2^128)"""
    size_additional = len(additional)*8
    size_ciphertext = len(ciphertext)*8

    if len(ciphertext) % block_size != 0:
        ciphertext += bytes(b'\x00' * (block_size - len(ciphertext)%block_size))
    if len(additional) % block_size != 0:
        additional += bytes(b'\x00' * (block_size - len(additional)%block_size))
    
    blocks = []
    blocks.extend([additional[block_size*i:(block_size*i)+block_size] for i in range(len(additional)//block_size)])
    blocks.extend([ciphertext[block_size*i:(block_size*i)+block_size] for i in range(len(ciphertext)//block_size)])
    blocks.append(i2b(size_additional, size=(block_size//2)*8, endian='big') + i2b(size_ciphertext, size=(block_size//2)*8, endian='big'))
    blocks = list(map(aes_polynomial, blocks))
    return blocks


def poly_blocks_to_aes_bytes(blocks, block_size=16):
    """Convert list of GF(2^128) to ciphertext"""
    blocks = list(map(lambda x: x.to_bytes(), blocks))
    sizes = blocks[-1]
    size_additional = b2i(sizes[:block_size//2], endian='big')
    size_ciphertext = b2i(sizes[block_size//2:], endian='big')
    size_additional_padded = size_additional//8
    if size_additional_padded % block_size != 0:
        size_additional_padded += 16 - size_additional_padded % block_size

    blocks = bytes(b''.join(blocks[:-1]))
    additional = blocks[:size_additional//8]
    ciphertext = blocks[size_additional_padded:size_additional_padded + size_ciphertext//8]
    return ciphertext, additional


def gcm_compute_parts(additional='', key=None, nonce=None, auth_key=None, s=None, plaintext='', ciphertext='', block_size=16):
    if nonce is not None and len(nonce) != 12:
        log.error('nonce length must be 12')
        return None, None, None

    if nonce is None or key is None:
        if None in (ciphertext, s):
            log.error('nonce can\'t be None if ciphertext, auth_key or s is None')
            return None, None, None

    blocks = []

    if auth_key is None:
        auth_key = bytes(AES.new(key, AES.MODE_ECB).encrypt(bytes(b'\x00'*block_size)))
    h = aes_polynomial(auth_key)

    if ciphertext == '':
        ciphertext = encrypt_ctr(plaintext, key, nonce, block_size, 2)

    size_additional = len(additional)*8
    size_ciphertext = len(ciphertext)*8

    if len(additional) % block_size != 0:
        additional += bytes(b'\x00'*(block_size - len(additional)%block_size))
    if len(ciphertext) % block_size != 0:
        ciphertext += bytes(b'\x00'*(block_size - len(ciphertext)%block_size))

    blocks.extend([additional[block_size*i:(block_size*i)+block_size] for i in range(len(additional)//block_size)])
    blocks.extend([ciphertext[block_size*i:(block_size*i)+block_size] for i in range(len(ciphertext)//block_size)])

    blocks.append(i2b(size_additional, size=(block_size//2)*8, endian='big') + i2b(size_ciphertext, size=(block_size//2)*8, endian='big'))

    blocks = map(aes_polynomial, blocks)

    g = aes_polynomial(0)
    for b in blocks:
        g = g + b
        g = g * h

    if s is None:
        s = bytes(AES.new(key, AES.MODE_ECB).encrypt(nonce+i2b(1, size=4*8, endian='big')))
    s = aes_polynomial(s)

    t = g + s
    return list(blocks), t, s


def gcm_encrypt(plaintext, additional, key, nonce, tag_size=128, block_size=16):
    if len(nonce) != 12:
        log.error('nonce length must be 12')
        return None, None

    ciphertext = encrypt_ctr(plaintext, key, nonce, block_size, 2)
    _, t, _ = gcm_compute_parts(ciphertext=ciphertext, additional=additional, key=key, nonce=nonce, block_size=16)

    return ciphertext, t.to_bytes()[:tag_size//8]


def gcm_verify(tag, ciphertext, additional, key, nonce, tag_size=16, block_size=16):
    _, t, _ = gcm_compute_parts(ciphertext=ciphertext, additional=additional, key=key, nonce=nonce, block_size=16)
    return t.to_bytes()[:tag_size//8], t.to_bytes()[:tag_size//8] == tag


def compute_s(tag, ciphertext, additional, auth_key):
    blocks = aes_bytes_to_poly_blocks(ciphertext, additional)
    t = aes_polynomial(tag)
    h = aes_polynomial(auth_key)

    g = aes_polynomial(0)
    for b in blocks:
        g = g + b
        g = g * h

    s = t - g
    return s.to_bytes()


def gcm_forge_tag(ciphertext, additional, auth_key, valid_ciphertext, valid_additional, valid_tag, tag_size=128):
    s = compute_s(valid_tag, valid_ciphertext, valid_additional, auth_key)
    blocks, t, s = gcm_compute_parts(ciphertext=ciphertext, additional=additional, auth_key=auth_key, s=s)
    return t.to_bytes()[:tag_size//8]


def derivate(f):
    if deg(f) == 0:
        return f.zero_element()
    return Polynomial_128([c*(i+1) for i,c in enumerate(f.coefficients[1:])])


def pth_root(f, p, w):
    return Polynomial_128([pow(a, p**(w-1)) for a in f.coefficients])


def polynomial_gcd(f, g):
    if f.is_one():
        return f
    if g.is_one():
        return g

    while deg(g) >= 0:
        t = g
        g = f % g
        f = t
    return f


def factor_square_free(f):
    # make it monic
    f = f.monic()

    # square free
    L = []
    s = 1
    p = 2
    w = f.k
    q = p**w
    while True:
        j = 1
        f_derivative = derivate(f)
        d = polynomial_gcd(f, f_derivative)
        g = f / d
        while not g.is_one():
            f /= g
            h = polynomial_gcd(f, g)
            m = g / h
            if not m.is_one():
                L.append((m, j*s))
            g = h
            j += 1
        if not f.is_one():
            f = pth_root(f, p, w)
            s = p*s
        if f.is_one():
            break
    return L


def factor_distinct_degree(f):
    L_dd = []
    h = f.element() % f
    k = 0
    q = 2**f.k
    while not f.is_one():
        h = h.powmod(q, f)
        k += 1
        g = polynomial_gcd(h-h.element(), f)
        if not g.is_one():
            L_dd.append((g, k))
            f /= g
            h %= f
    return L_dd


def random_polynomial(f):
    return Polynomial_128([GF_2k(randint(0, f.k), f.k, f.modulus) for _ in range(deg(f))]) % f


def factor_equal_degree(f, f_degree):
    n = deg(f)
    r = n / f_degree
    S = set([f])
    q = 2**f.k

    while len(S) < r:
        h = random_polynomial(f)
        g = polynomial_gcd(h, f)

        if g.is_one():
            g = h.modpow(((q**f_degree - 1)/3) - 1, f)

        S_tmp = set()
        for u in S:
            if deg(u) == f_degree:
                continue

            d = polynomial_gcd(g, u)
            if d.is_one() or d == u:
                S_tmp.add(u)
            else:
                S_tmp.update(set([d, u / d]))
        S = S_tmp
    return S


def factor_polynomial(f):
    log.debug('factoring {}'.format(f))
    factorization = []
    L_sf = factor_square_free(f)
    for f_sf, power_sf in L_sf:
        L_dd = factor_distinct_degree(f_sf)
        for f_dd, f_dd_degree in L_dd:
            L_ed = factor_equal_degree(f_dd, f_dd_degree)
            for f_ed in L_ed:
                factorization.append((f_ed, power_sf))
    return factorization


def recover_key_repated_nonce(ciphertexts_additionals_tags):
    """Recover authentication key for GCM given ciphertext encrypted with repeated nonce
    Sometimes fail (maybe bug in factorization)
    
    Args:
        ciphertexts_additionals_tags(list(tuple(bytes))): [(ciphertext, additional_data, auth_tag), ...]

    Returns:
        set(bytes): candidates for GCM auth key
    """
    auth_key_candidates = set()
    pair_count = 0
    for (ciphertext1, additional1, tag1), (ciphertext2, additional2, tag2) in combinations(ciphertexts_additionals_tags, 2):
        pair_count += 1
        log.debug('Trying pair no {}'.format(pair_count))
        p1 = aes_bytes_to_poly_blocks(ciphertext1, additional1)
        t1 = aes_polynomial(tag1)
        p1 = Polynomial_128([t1]+p1[::-1])    # first element is x0

        p2 = aes_bytes_to_poly_blocks(ciphertext2, additional2)
        t2 = aes_polynomial(tag2)
        p2 = Polynomial_128([t2]+p2[::-1])

        auth_key_candidates_tmp = set()
        factorization = factor_polynomial(p1+p2)
        for f, f_degree in factorization:
            if deg(f) == 1:
                log.debug('auth key candidate: {}'.format(f.monic()))
                key_candidate = f.monic().coefficients[0].to_bytes()
                auth_key_candidates_tmp.add(key_candidate)

        if len(auth_key_candidates) > 0: 
            auth_key_candidates.intersection_update(auth_key_candidates_tmp)
        else:
            auth_key_candidates = auth_key_candidates_tmp

        if len(auth_key_candidates) == 1:
            break

    log.success('Found {} auth key candidates'.format(len(auth_key_candidates)))
    return auth_key_candidates
