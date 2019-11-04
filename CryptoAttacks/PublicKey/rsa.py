from __future__ import absolute_import, division, print_function

import hashlib
import itertools
import math
import random
from builtins import bytes, hex, int, map, pow, range, str
from copy import deepcopy
from numbers import Number

import gmpy2
from Crypto.PublicKey import RSA as PyRSA

from CryptoAttacks.Math import (continued_fractions, convergents, crt, gcd,
                                invmod, pohlig_hellman, generate_smooth_prime)
from CryptoAttacks.Utils import b2i, i2b, i2h, log, power_of_two, random_bytes


class RSAKey(object):
    def __init__(self, n, e=0x10001, d=None, p=None, q=None, texts=None, identifier=None):
        """Construct key

        Args:
            n(long): RSA modulus
            e(long): Public exponent
            d(long): Private exponent (d). If key is private, one of d,p or q must be given
            p(long): First factor of n
            q(long): Second factor of n
            texts(list): list of dicts [{'cipher': 12332, 'plain': 65432423}, {'cipher': 0xffaa, 'plain': 0xbb11}]
                in encryption context, cipher == enc(plain)
                in signing context, cipher == sign(plain) 
            identifier(string/None): unique identifier of key

            self.size(int): bit size
        """
        if texts is None:
            texts = []
        self.texts = texts
        self.identifier = identifier or str(id(self))

        if d or p or q:
            if not d:
                if p:
                    q = n // p
                p = n // q
                d = int(invmod(e, (p - 1) * (q - 1)))
            else:
                if p or q:
                    if p:
                        q = n // p
                    p = n // q
                else:
                    p, q = factors_from_d(n, e, d)
            tup = (n, e, d, p, q)
        else:
            tup = (n, e)
        tup = list(map(int, tup))

        self.n, self.e, self.d, self.p, self.q = n, e, d, p, q
        self.size = int(math.ceil(math.log(n, 2) / 8.0) * 8)
        self.pyrsa_key = PyRSA.construct(tup)

    def encrypt(self, plaintext):
        """Raw encryption

        Args: plaintext(int/string)
        Returns: pow(plaintext,e,n)
        """
        if not isinstance(plaintext, Number):
            try:
                plaintext = b2i(plaintext)
            except:
                log.critical_error(
                    "Plaintext to decrypt must be number or be convertible to number ({})".format(plaintext))
        return self.pyrsa_key.encrypt(int(plaintext), 0)[0]

    def decrypt(self, ciphertext):
        """Raw decryption

        Args: ciphertext(int/string)
        Returns: pow(ciphertext, d, n)
        """
        if not isinstance(ciphertext, Number):
            try:
                ciphertext = b2i(ciphertext)
            except:
                log.critical_error(
                    "Ciphertext to decrypt must be number or be convertible to number ({})".format(ciphertext))
        return self.pyrsa_key.decrypt(int(ciphertext))

    def copy(self, identifier=''):
        if self.has_private():
            tmp_key = RSAKey(self.n, self.e, self.d, self.p, self.q, identifier=identifier)
        else:
            tmp_key = RSAKey(self.n, self.e, identifier=identifier)
        tmp_key.texts = deepcopy(self.texts)
        return tmp_key

    def publickey(self, identifier=''):
        """Extract public key"""
        derived_public_key = RSAKey(self.n, self.e, identifier=identifier + ' - publickey')
        derived_public_key.texts = deepcopy(self.texts)
        return derived_public_key

    def has_private(self):
        return any([self.d, self.p, self.q])

    def add_ciphertext(self, ciphertext, position=None):
        """Args:
            ciphertext(int/string)
            position(int/None) - position in list where to add, None for new
        """
        if not isinstance(ciphertext, Number):
            try:
                ciphertext = b2i(ciphertext)
            except:
                log.critical_error(
                    "Ciphertext to add must be number or be convertible to number ({})".format(ciphertext))
        if position is None:
            self.texts.append({'cipher': ciphertext})
        else:
            self.texts[position]['cipher'] = ciphertext

    def add_plaintext(self, plaintext, position=None):
        """Args:
            plaintext(int/string)
            position(int/None) - position in list where to add, None for new
        """
        if not isinstance(plaintext, Number):
            try:
                plaintext = b2i(plaintext)
            except:
                log.critical_error("Plaintext to add must be number or be convertible to number ({})".format(plaintext))
        if position is None:
            self.texts.append({'plain': plaintext})
        else:
            self.texts[position]['plain'] = plaintext

    def add_text_pair(self, ciphertext=None, plaintext=None):
        """Args: ciphertext(int), plaintext(int)"""
        if not ciphertext and not plaintext:
            log.error("Can't add None ciphertext and None plaintext")
            return

        text_pair = {}
        if ciphertext:
            if not isinstance(ciphertext, Number):
                log.error("Ciphertext to add have to be number")
            else:
                text_pair['cipher'] = ciphertext
        if plaintext:
            if not isinstance(plaintext, Number):
                log.error("Plaintext to add have to be number")
            else:
                text_pair['plain'] = plaintext
        self.texts.append(text_pair)

    def clear_texts(self):
        self.texts = []

    def print_texts(self):
        print("key {} texts:".format(self.identifier))
        for pair in self.texts:
            if 'cipher' in pair:
                print("Ciphertext: {}".format(hex(pair['cipher'])), end=", ")
            else:
                print("Ciphertext: null", end=", ")
            if 'plain' in pair:
                print("Plaintext: {} (\"{}\")".format(hex(pair['plain']), i2b(pair['plain'], size=self.size)))
            else:
                print("Plaintext: null")

    def __str__(self):
        if self.has_private():
            return str(self.identifier) + " (private)"
        else:
            return str(self.identifier) + " (public)"

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def generate(bits, e=0x10001, randfunc=None, progress_func=None, identifier=None):
        """
        bits(int): key size
        e(int): public exponent
        randfunc(callable)
        progress_func(callable)
        identifier(string/None): unique identifier of key
        """
        tmp_key = PyRSA.generate(bits, e=int(e), randfunc=randfunc, progress_func=progress_func)
        return RSAKey(tmp_key.n, tmp_key.e, tmp_key.d, tmp_key.p, tmp_key.q, identifier=identifier)

    @staticmethod
    def construct(n, e=0x10001, d=None, p=None, q=None, identifier=None):
        """Construct key

        Args:
            n(long): RSA modulus
            e(long): Public exponent
            d(long): Private exponent (d). If key is private, one of d,p or q must be given
            p(long): First factor of n
            q(long): Second factor of n
            identifier(string/None): unique identifier of key
        Returns:
            RSAKey
        """
        return RSAKey(n, e, d, p, q, identifier=identifier)

    @staticmethod
    def import_key(filename, identifier=None, *args, **kwargs):
        """Import key from file

        Args:
            filename(string): use it as key's id
            identifier(string/None): unique identifier of key
        Returns:
            RSAKey
        """
        if identifier is None:
            identifier = filename
        tmp_key = PyRSA.importKey(open(filename).read())
        if hasattr(tmp_key, 'p'):
            return RSAKey(tmp_key.n, tmp_key.e, p=tmp_key.p, identifier=identifier)
        else:
            return RSAKey(tmp_key.n, tmp_key.e, identifier=identifier)

    def export_key(self, format='PEM', passphrase=None, pkcs=1, *args, **kwargs):
        """Export key as string"""
        return self.pyrsa_key.exportKey(format, passphrase, pkcs)


def _prepare_ciphertexts(key=None, ciphertext=None, ciphertexts=None):
    """Helper function used in various rsa functions.
        Update key (if provided) and yield ciphertexts to crack

    Yields:
        tuple: (text_no, ciphertext_to_crack)
    """
    if ciphertexts is None:
        ciphertexts = []
    if ciphertext is not None:
        ciphertexts.append(ciphertext)

    if key is None:
        for cipher in ciphertexts:
            yield None, cipher
    else:
        for cipher in ciphertexts:
            matching_texts = [(text_no, text) for text_no, text in enumerate(key.texts) if
                              'cipher' in text and text['cipher'] == cipher]
            if len(matching_texts) == 0:
                key.add_ciphertext(cipher)
                yield len(key.texts) - 1, cipher
            else:
                assert len(matching_texts) == 1
                text_no, text = matching_texts
                if 'plain' in text:
                    log.success("Plaintext for ciphertext {cipher} already known: {plain}!".format(**text))
                else:
                    yield text_no, cipher


def factors_from_d(n, e, d):
    """Factorize n to p and q given e and d"""
    k = e * d - 1
    while True:
        g = random.randint(2, n - 2)
        b = k // (2 ** power_of_two(k))
        while b < k:
            gb = pow(g, b, n)
            if gb != 1 and gb != n - 1 and pow(gb, 2, n) == 1:
                if gcd(gb - 1, n) != 1:
                    p = gcd(gb - 1, n)
                else:
                    p = gcd(gb + 1, n)
                return p, n // p
            b *= 2


def get_mutable_texts(key, texts):
    if texts is None:
        return [key_texts['cipher'] for key_texts in key.texts if 'cipher' in key_texts and 'plain' not in key_texts]
    return texts


def small_e_msg(key, ciphertexts=None, max_times=100):
    """If both e and plaintext are small, ciphertext may exceed modulus only a little

    Args:
        key(RSAKey): with small e, at least one ciphertext
        ciphertexts(list)
        max_times(int): how many times plaintext**e exceeded modulus maximally

    Returns:
        list: recovered plaintexts
    """
    ciphertexts = get_mutable_texts(key, ciphertexts)
    recovered = []
    for ciphertext in ciphertexts:
        log.debug("Find msg for ciphertext {}".format(ciphertext))
        times = 0
        for k in range(max_times):
            msg, is_correct = gmpy2.iroot(ciphertext + times, key.e)
            if is_correct and pow(msg, key.e, key.n) == ciphertext:
                msg = int(msg)
                log.success("Found msg: {}, times=={}".format(i2h(msg), times // key.n))
                recovered.append(msg)
                break
            times += key.n
    return recovered


def common_primes(keys):
    """Find common prime in keys modules

    Args:
        keys(list): RSAKeys

    Returns:
        list: RSAKeys for which factorization of n was found
    """
    priv_keys = []
    for pair in itertools.combinations(keys, 2):
        prime = gmpy2.gcd(pair[0].n, pair[1].n)
        if prime != 1:
            log.success("Found common prime in: {}, {}".format(pair[0].identifier, pair[1].identifier))
            for key_no in range(2):
                if pair[key_no] not in priv_keys:
                    d = int(invmod(pair[key_no].e, (prime - 1) * (pair[key_no].n // prime - 1)))
                    new_key = RSAKey.construct(int(pair[key_no].n), int(pair[key_no].e), int(d),
                                               identifier=pair[key_no].identifier + '-private')
                    new_key.texts = pair[key_no].texts[:]
                    priv_keys.append(new_key)
                else:
                    log.debug("Key {} already in priv_keys".format(pair[key_no].identifier))
    return priv_keys


def wiener(key):
    """Wiener small private exponent attack
     If d < (1/3)*(N**(1/4)), d can be effectively recovered using continuous fractions

     Args:
        key(RSAKey): public rsa key to break

    Returns:
        NoneType/RSAKey: None if didn't break key, private key otherwise
    """
    en_fractions = continued_fractions(key.e, key.n)
    for k, d in convergents(en_fractions):
        if k != 0 and (key.e * d - 1) % k == 0:
            phi = (key.e * d - 1) // k
            """ p**2 - p*(n - phi + 1) + n == 0 """
            b = key.n - phi + 1
            delta = b * b - 4 * key.n
            if delta > 0:
                sqrt_delta = gmpy2.isqrt(delta)
                if sqrt_delta * sqrt_delta == delta and sqrt_delta % 2 == 0:
                    log.debug("Found private key (d={}) for {}".format(d, key.identifier))
                    new_key = RSAKey.construct(key.n, key.e, d, identifier=key.identifier + '-private')
                    new_key.texts = key.texts[:]
                    return new_key
    return None


def hastad(keys, ciphertexts=None):
    """Hastad's broadcast attack (small public exponent)
    Given at least e keys with public exponent equals to e and ciphertexts of the same plaintext,
    plaintext can be efficiently recovered

    Args:
        keys(list): RSAKeys, all with same public exponent e, len(keys) >= e,
                    every key with only one ciphertext
        ciphertexts(list/None): if not None, use this ciphertexts

    Returns:
        NoneType/int: None on failure, recovered plaintext otherwise
        update keys texts
    """
    e = keys[0].e
    if len(keys) < e:
        log.critical_error("Not enough keys, e={}".format(e))

    if ciphertexts is None:
        for key in keys:
            if len(key.texts) != 1:
                log.info("Key have more than one ciphertext, using the first one(key=={})".format(key.identifier))
            if 'cipher' not in key.texts[0]:
                log.critical_error("key {} doesn't have ciphertext".format(key.identifier))

        # prepare ciphertexts and correct_keys lists
        ciphertexts, modules, correct_keys = [], [], []
        for key in keys:
            # get only first ciphertext (if exists)
            if key.n not in modules and key.texts[0]['cipher'] not in ciphertexts:
                if key.e == e:
                    modules.append(key.n)
                    correct_keys.append(key)
                    ciphertexts.append(key.texts[0]['cipher'])
                else:
                    log.info("Key {} have different e(={})".format(key.identifier, key.e))
    else:
        if len(ciphertexts) != len(keys):
            log.critical_error("len(ciphertexts) != len(keys)")
        modules = [key.n for key in keys]
        correct_keys = keys

    # check if we have enough ciphertexts
    if len(modules) < e:
        log.info("Not enough keys with unique modulus and ciphertext, e={}, len(modules)={}".format(e, len(modules)))
        log.info("Checking for simple roots (small_e_msg)")
        for one_key in correct_keys:
            recovered_plaintexts = small_e_msg(one_key)
            if len(recovered_plaintexts) > 0:
                log.success("Found plaintext: {}".format(recovered_plaintexts[0]))
                return recovered_plaintexts[0]

    if len(modules) > e:
        log.debug("Number of modules/ciphertexts larger than e")
        modules = modules[:e]
        ciphertexts = ciphertexts[:e]

    # actual Hastad
    result = crt(ciphertexts, modules)
    plaintext, correct = gmpy2.iroot(result, e)
    if correct:
        plaintext = int(plaintext)
        log.success("Found plaintext: {}".format(plaintext))
        for one_key in correct_keys:
            one_key.texts[0]['plain'] = plaintext
        return plaintext
    else:
        log.debug("Plaintext wasn't {}-th root")
        log.debug("result (from crt) = {}".format(e, result))
        log.debug("plaintext ({}-th root of result) = {}".format(e, plaintext))
        return None


def faulty(key, padding=None):
    """Faulty attack against crt-rsa, Boneh-DeMillo-Lipton
    sp = padding(m)**(d % p-1) % p
    sq' = padding(m)**(d % q-1) % q <--any error during computation
    s' = crt(sp, sq') % n <-- broken signature
    s = crt(sp, sq) % n <-- correct signature
    p = gcd(s'**e - padding(m), n)
    p = gcd(s - s', n)

    Args:
        key(RSAKey): with at least one broken signature (key.texts[no]['cipher']) and corresponding
                     plaintext (key.texts[no]['plain']), or valid and broken signature
        padding(None/function): function used before signing message

    Returns:
        NoneType/RSAKey: False on failure, recovered private key otherwise
    """
    log.debug("Check signature-message pairs")
    for pair in key.texts:
        if 'plain' in pair and 'cipher' in pair:
            signature = gmpy2.mpz(pair['cipher'])
            message = pair['plain']
            if padding:
                message = padding(message)
            p = gmpy2.gcd(pow(signature, key.e) - message, key.n)
            if p != 1 and p != key.n:
                log.info("Found p={}".format(p))
                new_key = RSAKey.construct(key.n, key.e, p=p, identifier=key.identifier + '-private')
                new_key.texts = key.texts[:]
                return new_key

    log.debug("Check for valid-invalid signatures")
    signatures = [tmp['cipher'] for tmp in key.texts if 'cipher' in tmp]
    for pair in itertools.combinations(signatures, 2):
        p = gmpy2.gcd(pair[0] - pair[1], key.n)
        if p != 1 and p != key.n:
            log.info("Found p={}".format(p))
            new_key = RSAKey.construct(key.n, key.e, p=p, identifier=key.identifier + '-private')
            new_key.texts = key.texts[:]
            return new_key
    return None


def parity_oracle(ciphertext):
    """Function implementing parity oracle

    Args:
        ciphertext(int)

    Returns:
        int: 0 (if decrypted ciphertext is even) or 1 (is odd)
    """
    raise NotImplementedError


def parity(parity_oracle, key, min_lower_bound=None, max_upper_bound=None):
    """Given oracle that returns LSB of decrypted ciphertext we can decrypt whole ciphertext
    parity_oracle function must be implemented

    Args:
        parity_oracle(callable)
        key(RSAKey): contains ciphertexts to decrypt
        min_lower_bound(None/int)
        max_upper_bound(None/int)

    Returns:
        dict: decrypted ciphertexts
        update key texts
    """
    try:
        parity_oracle(1)
    except NotImplementedError:
        log.critical_error("Parity oracle not implemented")

    recovered = {}
    for text_no in range(len(key.texts)):
        if 'cipher' in key.texts[text_no] and 'plain' not in key.texts[text_no]:
            cipher = key.texts[text_no]['cipher']
            log.info("Decrypting {}".format(cipher))
            two_encrypted = key.encrypt(2)

            counter = lower_bound = numerator = 0
            upper_bound = key.n
            denominator = 1
            while lower_bound + 1 < upper_bound:
                cipher = (two_encrypted * cipher) % key.n
                denominator *= 2
                numerator *= 2
                counter += 1

                if max_upper_bound is not None and upper_bound > max_upper_bound:
                    is_odd = 0
                else:
                    # todo: check below
                    if min_lower_bound is not None and lower_bound < min_lower_bound:
                        is_odd = 1
                    else:
                        is_odd = parity_oracle(cipher)

                if is_odd:  # plaintext > n/(2**counter)
                    numerator += 1
                lower_bound = (key.n * numerator) // denominator
                upper_bound = (key.n * (numerator + 1)) // denominator

                log.debug("{} {} [{}, {}]".format(counter, is_odd, int(lower_bound), int(upper_bound)))
                log.debug("{}/{}  -  {}/{}\n".format(numerator, denominator, numerator + 1, denominator))
            log.success("Decrypted: {}".format(i2h(upper_bound)))
            key.texts[text_no]['plain'] = upper_bound
            recovered[text_no] = upper_bound
    return recovered


def signing_oracle(plaintext):
    """Function implementing signing oracle

    Args:
        plaintext(int)

    Returns:
        int: signature of given plaintext
    """
    raise NotImplementedError


def decryption_oracle(ciphertext):
    """Function implementing decryption oracle

    Args:
        ciphertext(int)

    Returns:
        int: decrypted ciphertext
    """
    raise NotImplementedError


def blinding(key, signing_oracle=None, decryption_oracle=None):
    """Perform signature/ciphertext blinding attack

    Args:
        key(RSAKey): with at least one plaintext(to sign) or ciphertext(to decrypt)
        signing_oracle(callable)
        decryption_oracle(callable)

    Returns:
        dict: {index: signature/plaintext, index2: signature/plaintext}
        update key texts
    """
    if not signing_oracle and not decryption_oracle:
        log.critical_error("Give one of signing_oracle or decryption_oracle")
    if signing_oracle and decryption_oracle:
        log.critical_error("Give only one of signing_oracle or decryption_oracle")

    recovered = {}
    if signing_oracle:
        log.debug("Have signing_oracle")
        for text_no in range(len(key.texts)):
            if 'plain' in key.texts[text_no] and 'cipher' not in key.texts[text_no]:
                log.info("Blinding signature of plaintext no {} ({})".format(text_no, i2h(key.texts[text_no]['plain'])))

                blind = random.randint(2, 100)
                blind_enc = key.encrypt(blind)
                blinded_plaintext = (key.texts[text_no]['plain'] * blind_enc) % key.n
                blinded_signature = signing_oracle(blinded_plaintext)
                if not blinded_signature:
                    log.critical_error("Error during call to signing_oracle({})".format(blinded_plaintext))
                signature = (invmod(blind, key.n) * blinded_signature) % key.n
                key.texts[text_no]['cipher'] = signature
                recovered[text_no] = signature
                log.success("Signature: {}".format(signature))

    if decryption_oracle:
        log.debug("Have decryption_oracle")
        for text_no in range(len(key.texts)):
            if 'cipher' in key.texts[text_no] and 'plain' not in key.texts[text_no]:
                log.info("Blinding ciphertext no {} ({})".format(text_no, key.texts[text_no]['cipher']))
                blind = random.randint(2, 100)
                blind_enc = key.encrypt(blind)
                blinded_ciphertext = (key.texts[text_no]['cipher'] * blind_enc) % key.n
                blinded_plaintext = decryption_oracle(blinded_ciphertext)
                if not blinded_plaintext:
                    log.critical_error("Error during call to decryption_oracle({})".format(blinded_plaintext))
                plaintext = (invmod(blind, key.n) * blinded_plaintext) % key.n
                key.texts[text_no]['plain'] = plaintext
                recovered[text_no] = plaintext
                log.success("Plaintext: {}".format(plaintext))

    return recovered


def bleichenbacher_signature_forgery(key, garbage='suffix', hash_function='sha1'):
    """Bleichenbacher's signature forgery based on bug in verify implementation

    Args:
        key(RSAKey): with small e and at least one plaintext
        garbage(string): middle: 00 01 ff garbage 00 ASN.1 HASH
                         suffix: 00 01 ff 00 ASN.1 HASH garbage
        hash_function(string)

    Returns:
        dict: forged signatures, signatures[no] == signature(key.texts[no]['plain'])
        update key texts
    """
    hash_asn1 = {
        'md5': bytes(b'\x30\x20\x30\x0c\x06\x08\x2a\x86\x48\x86\xf7\x0d\x02\x05\x05\x00\x04\x10'),
        'sha1': bytes(b'\x30\x21\x30\x09\x06\x05\x2b\x0e\x03\x02\x1a\x05\x00\x04\x14'),
        'sha256': bytes(b'\x30\x31\x30\x0d\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x01\x05\x00\x04\x20'),
        'sha384': bytes(b'\x30\x41\x30\x0d\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x02\x05\x00\x04\x30'),
        'sha512': bytes(b'\x30\x51\x30\x0d\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x03\x05\x00\x04\x40')
    }
    if garbage not in ['suffix', 'middle']:
        log.critical_error("Bad garbage position, must be suffix or middle")
    if hash_function not in list(hash_asn1.keys()):
        log.critical_error("Hash function {} not implemented".format(hash_function))

    if key.e > 3:
        log.debug("May not work, because e > 3")

    signatures = {}
    if garbage == 'suffix':
        for text_no in range(len(key.texts)):
            if 'plain' in key.texts[text_no] and 'cipher' not in key.texts[text_no]:
                log.info("Forge for plaintext no {} ({})".format(text_no, key.texts[text_no]['plain']))

                hash_callable = getattr(hashlib, hash_function)(
                    i2b(key.texts[text_no]['plain'])).digest()  # hack to call hashlib.hash_function
                plaintext_prefix = bytes(b'\x00\x01\xff\x00') + hash_asn1[hash_function] + hash_callable

                plaintext = plaintext_prefix + bytes(b'\x00' * (key.size // 8 - len(plaintext_prefix)))
                plaintext = b2i(plaintext)
                for round_error in range(-5, 5):
                    signature, _ = gmpy2.iroot(plaintext, key.e)
                    signature = int(signature + round_error)
                    test_prefix = i2b(pow(signature, key.e, key.n), size=key.size)[:len(plaintext_prefix)]
                    if test_prefix == plaintext_prefix:
                        log.info("Got signature: {}".format(signature))
                        log.debug("signature**e % n == {}".format(i2h(pow(signature, key.e, key.n), size=key.size)))
                        key.texts[text_no]['cipher'] = signature
                        signatures[text_no] = signature
                        break
                else:
                    log.error("Something wrong, can't compute correct signature")
        return signatures

    elif garbage == 'middle':
        for text_no in range(len(key.texts)):
            if 'plain' in key.texts[text_no] and 'cipher' not in key.texts[text_no]:
                log.info("Forge for plaintext no {} ({})".format(text_no, key.texts[text_no]['plain']))
                hash_callable = getattr(hashlib, hash_function)(
                    i2b(key.texts[text_no]['plain'])).digest()  # hack to call hashlib.hash_function
                plaintext_suffix = bytes(b'\x00') + hash_asn1[hash_function] + hash_callable
                if b2i(plaintext_suffix) & 1 != 1:
                    log.error("Plaintext suffix is even, can't compute signature")
                    continue

                # compute suffix
                signature_suffix = 0b1
                for b in range(len(plaintext_suffix) * 8):
                    if (signature_suffix ** 3) & (1 << b) != b2i(plaintext_suffix) & (1 << b):
                        signature_suffix |= 1 << b
                signature_suffix = i2b(signature_suffix)[-len(plaintext_suffix):]

                # compute prefix
                while True:
                    plaintext_prefix = bytes(b'\x00\x01\xff') + random_bytes(key.size // 8 - 3)
                    signature_prefix, _ = gmpy2.iroot(b2i(plaintext_prefix), key.e)
                    signature_prefix = i2b(int(signature_prefix), size=key.size)[:-len(signature_suffix)]

                    signature = b2i(signature_prefix + signature_suffix)
                    test_plaintext = i2b(pow(signature, key.e, key.n), size=key.size)
                    if bytes(b'\x00') not in test_plaintext[2:-len(plaintext_suffix)]:
                        if test_plaintext[:3] == plaintext_prefix[:3] and test_plaintext[
                                                                          -len(plaintext_suffix):] == plaintext_suffix:
                            log.info("Got signature: {}".format(signature))
                            key.texts[text_no]['cipher'] = signature
                            signatures[text_no] = signature
                            break
                        else:
                            log.error("Something wrong, signature={},"
                                      " signature**{}%{} is {}".format(signature, key.e, key.n, [(test_plaintext)]))
                            break
        return signatures


def dsks(message, signature, n, smooth_bit_size=30, hash_function=None):
    """Duplicate-Signature Key Selection on RSA
    Create key pair verifies given signature

    signature^e == hash_function(message) % n

    So if we have someone's public key (with n) and signature s of some message signed
    with corresponding private key we can create new key pair that will verify the signature,
    BUT new e will be large

    Can also be used stuff like generating key pair that will decrypt given message to choosen plaintext

    Args:
        message(int/arg for hash_function)
        signature(int)
        n(int)
        smooth_bit_size(int): to tweak, most factors of p-1 and q-1 will be of this bit size 
        hash_function(NoneType/callable): converting message to int

    Returns:
        tuple(int): n', factors of p'-1, factors of q'-1, e', d'
    """
    m = message
    s = signature

    key_size = n.bit_length() + 1

    while True:
        p, p_order_factors = generate_smooth_prime(key_size // 2,
                                                   primitive_roots=[m, s], smooth_bit_size=smooth_bit_size)
        q, q_order_factors = generate_smooth_prime(key_size - p.bit_length() + 1,
                                                   primitive_roots=[m, s], smooth_bit_size=smooth_bit_size,
                                                   exclude=p_order_factors)
        n_p = p * q

        if n_p > n:
            log.debug("n generated")
            log.debug("n' = {}".format(n_p, n_p.bit_length()))
            log.debug("p' = {}".format(p, p_order_factors))
            log.debug("q' = {}".format(q, q_order_factors))

            ep = pohlig_hellman(s, m, p, p_order_factors)
            eq = pohlig_hellman(s, m, q, q_order_factors)
            log.debug("ep' = {}".format(ep))
            log.debug("eq' = {}".format(eq))

            e = crt([ep, eq], [p - 1, (q - 1) // 2])
            log.debug("e' = {}".format(e))

            d = invmod(e, (p - 1) * (q - 1))
            log.debug("d' = {}".format(d))
            return n_p, p_order_factors, q_order_factors, e, d
        else:
            print('nope', float(n_p) / float(n))


def pkcs15_padding_oracle(ciphertext):
    """Function implementing PKCS 1.5 Padding Oracle

    Args:
        ciphertext(int)

    Returns:
        bool: True if decrypted ciphertext has correct padding (starts with 0x0002 at least), False otherwise
    """
    raise NotImplementedError


def bleichenbacher_pkcs15(pkcs15_padding_oracle, key, ciphertext=None):
    """Given oracle that checks if ciphertext decrypts to some valid plaintext with PKCS1.5 padding
    we can decrypt whole ciphertext
    pkcs15_padding_oracle function must be implemented

    http://archiv.infsec.ethz.ch/education/fs08/secsem/bleichenbacher98.pdf

    Args:
        pkcs15_padding_oracle(callable)
        key(RSAKey): contains ciphertexts to decrypt

    Returns:
        dict: decrypted ciphertexts
        update key texts
    """
    try:
        pkcs15_padding_oracle(1)
    except NotImplementedError:
        log.critical_error("PKCS1.5 padding oracle not implemented")

    def ceil(a, b):
        return a // b + (a % b > 0)

    def floor(a, b):
        return a // b

    def update_intervals(M, B, s, n):
        # step 3
        M2 = []
        for Mi in M:
            a, b = Mi
            for r in range(ceil(a * s - 3 * B + 1, n), ceil(b * s - 2 * B, n) + 1):
                M2.append((max(a, ceil(2 * B + r * n, s)), min(b, floor(3 * B - 1 + r * n, s))))
        return M2

    recovered = {}
    for text_no, cipher in _prepare_ciphertexts(key=key, ciphertext=ciphertext):
        log.info("Decrypting {}".format(cipher))

        n = key.n
        e = key.e
        B = pow(2, key.size - 2)

        # blind it
        log.debug('Blinding the ciphertext')
        s0 = 1
        cipher0 = cipher
        while not pkcs15_padding_oracle(cipher0):
            s0 += 1
            cipher0 = (cipher * pow(s0, e, n)) % n
        M0 = [(2 * B, 3 * B - 1)]
        i = 1
        log.debug('Found s0: {}'.format(hex(s0)))

        # step 2.a
        s1 = n / (3 * B)
        cipher1 = (cipher0 * pow(s1, e, n)) % n
        while not pkcs15_padding_oracle(cipher1):
            s1 += 1
            cipher1 = (cipher0 * pow(s1, e, n)) % n
        Mi = update_intervals(M0, B, s1, n)
        si = s1
        i += 1

        interval_narrowed = False
        while not interval_narrowed:
            if len(Mi) == 0:
                log.error("Something wrong, len(Mi) == 0")
                return None

            elif len(Mi) > 1:
                # step 2.b
                si = si + 1
                cipheri = (cipher0 * pow(si, e, n)) % n
                while not pkcs15_padding_oracle(cipheri):
                    s1 += 1
                    cipheri = (cipher0 * pow(si, e, n)) % n

            else:
                # step 2.c
                a, b = Mi[0]

                if a != b:
                    si_found = False
                    while not si_found:
                        ri = ceil(2 * (b * si - 2 * B), n)
                        for si in range(ceil(2 * B + ri * n, b), ceil(3 * B + ri * n, a) + 1):
                            cipheri = (cipher0 * pow(si, e, n)) % n
                            if pkcs15_padding_oracle(cipheri):
                                si_found = True
                                break

                else:
                    # step 4
                    log.success("Interval narrowed to one value")
                    log.debug("plaintext = {}".format(hex(a)))
                    interval_narrowed = True

            Mi = update_intervals(Mi, B, si, n)

        recovered[ciphertext] = Mi[0][0]
        key.texts[text_no]['plain'] = recovered[ciphertext]

    return recovered
