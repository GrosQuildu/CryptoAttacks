import itertools
from copy import deepcopy

from Crypto.PublicKey import RSA as PyRSA
from CryptoAttacks.Math import *
from CryptoAttacks.Utils import *


class RSAKey(PyRSA._RSAobj):
    def __init__(self):
        """
        self.texts: list of dict [{'cipher': 12332, 'plain': 65432423}, {'cipher': 0xffaa, 'plain': 0xbb11}]
        self.identifier: id(self), filename or custom
        """
        self.texts = []
        self.identifier = ''

    def encrypt(self, plaintext):
        """Raw encryption
        Args: plaintext(int)
        Returns: pow(plaintext,e,n)
        """
        return pow(plaintext, self.e, self.n)

    def decrypt(self, ciphertext):
        """Raw decryption
        Args: ciphertext
        Returns: pow(ciphertext, d, n)
        """
        return pow(ciphertext, self.d, self.n)

    def copy(self, identifier=''):
        if self.has_private():
            tmp = RSAKey.construct(self.n, self.e, self.d, self.p, self.q, identifier=identifier)
            tmp.texts = deepcopy(self.texts)
        else:
            tmp = RSAKey.construct(self.n, self.e, identifier=identifier)
            tmp.texts = deepcopy(self.texts)
        return tmp

    def publickey(self, identifier=''):
        """Extract public key"""
        tmp = RSAKey.construct(self.n, self.e, identifier=identifier)
        tmp.texts = deepcopy(self.texts)
        return tmp

    def add_ciphertext(self, ciphertext):
        self.texts.append({'cipher': ciphertext})

    def add_plaintext(self, plaintext):
        self.texts.append({'plain': plaintext})

    def add_text_pair(self, ciphertext=None, plaintext=None):
        if not ciphertext and not plaintext:
            log.error("Can't add None ciphertext and None plaintext")
        tmp = {}
        if ciphertext:
            tmp['cipher'] = ciphertext
        if plaintext:
            tmp['plain'] = plaintext
        self.texts.append(tmp)

    @staticmethod
    def generate(bits, e=0x10001, randfunc=None, progress_func=None, identifier=None):
        """
        bits(int): key size
        e(int): public exponent
        randfunc(function)
        progress_func(function)
        identifier(string/None): unique identifier of key
        """
        tmp_key = PyRSA.generate(bits, e=e, randfunc=randfunc, progress_func=progress_func)
        tmp_key.__class__ = RSAKey
        tmp_key.__init__()
        if identifier:
            tmp_key.identifier = identifier
        else:
            tmp_key.identifier = str(id(tmp_key))
        return tmp_key

    @staticmethod
    def construct(n, e=0x10001, d=None, p=None, q=None, identifier=None):
        """Construct key from tuple

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
        if d or p or q:
            if not d:
                p = p or q
                d = long(gmpy2.invert(e, (p - 1)*(n/p - 1)))
            tup = (n, e, d)
        else:
            tup = (n, e)
        tup = map(long, tup)

        tmp_key = PyRSA.construct(tup)
        tmp_key.__class__ = RSAKey
        tmp_key.__init__()
        if identifier:
            tmp_key.identifier = identifier
        else:
            tmp_key.identifier = str(id(tmp_key))
        return tmp_key

    @staticmethod
    def import_key(filename, identifier=None, *args, **kwargs):
        """Import key from file

        Args:
            filename(string): use it as key's id
            identifier(string/None): unique identifier of key
        Returns:
            RSAKey
        """
        tmp_key = PyRSA.importKey(open(filename).read(), *args, **kwargs)
        tmp_key.__class__ = RSAKey
        tmp_key.__init__()
        if identifier:
            tmp_key.identifier = identifier
        else:
            tmp_key.identifier = filename
        return tmp_key


def small_e_msg(key, max_times=100):
    """If both e and plaintext are small, ciphertext may exceed modulus a little

    Args:
        key(RSAKey): with small e, at least one ciphertext
        max_times(int): how many times plaintext**e exceeded modulus

    Returns:
        dict: recovered plaintexts
        update key texts with found plaintexts
    """
    recovered = []
    for text_no in range(len(key.texts)):
        if 'cipher' in key.texts[text_no] and 'plain' not in key.texts[text_no]:
            cipher = key.texts[text_no]['cipher']
            log.debug("Find msg for ciphertext {}".format(cipher))
            times = 0
            for k in range(max_times):
                msg, is_correct = gmpy2.iroot(cipher+times, key.e)
                if is_correct:
                    msg = long(msg)
                    log.success("Found msg: {}, times=={}".format(i2b(msg), times))
                    key.texts[text_no]['plain'] = msg
                    recovered[text_no] = msg
                    break
                times += key.n
    return recovered


def common_primes(keys):
    """Find common prime in keys modules

    Args:
        keys(list):  RSAKeys

    Returns:
        list:  RSAKeys for which factorization of n was found
    """
    priv_keys = []
    for pair in itertools.combinations(keys, 2):
        prime = gmpy2.gcd(pair[0].n, pair[1].n)
        if prime != 1:
            log.info("Found common prime in: {}, {}".format(pair[0].identifier, pair[1].identifier))
            for key_no in xrange(2):
                if pair[key_no] not in priv_keys:
                    d = long(gmpy2.invert(pair[key_no].e, (prime - 1) * (pair[key_no].n/prime - 1)))
                    new_key = RSAKey.construct(long(pair[key_no].n), long(pair[key_no].e), long(d), identifier=pair[key_no].identifier+'-private')
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
        bool/RSAKey: False if didn't break key, private key otherwise
    """
    en_fractions = continued_fractions(key.e, key.n)
    for k, d in convergents(en_fractions):
        if k != 0 and (key.e * d - 1) % k == 0:
            phi = (key.e * d - 1) // k
            """ p**2 - p*(n - phi + 1) + n == 0 """
            b = key.n - phi + 1
            delta = b*b - 4*key.n
            if delta > 0:
                sqrt_delta = gmpy2.isqrt(delta)
                if sqrt_delta*sqrt_delta == delta and sqrt_delta % 2 == 0:
                    log.debug("Found private key (d={}) for {}".format(d, key.identifier))
                    new_key = RSAKey.construct(long(key.n), long(key.e), long(d), identifier=key.identifier+'-private')
                    new_key.texts = key.texts[:]
                    return new_key
    return False


def hastad(keys):
    """Hastad's broadcast attack (small public exponent)
    Given at least e keys with public exponent equals to e and ciphertexts of the same plaintext,
    plaintext can be efficiently recovered

    Args:
        keys(list): RSAKeys, all with same public exponent e, len(keys) >= e,
                    every key with only one ciphertext

    Returns:
        bool/string: False on failure, recovered plaintext otherwise
        update keys texts
    """
    e = keys[0].e
    if len(keys) < e:
        log.critical_error("Not enough keys, e={}".format(e))

    for key in keys:
        if len(key.texts) != 1:
            log.critical_error("Only one ciphertext per key allowed (key=={})".format(key.identifier))
        if 'plain' in key.texts[0]:
            log.critical_error("key {} have plaintext already".format(key.identifier))
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
        plaintext = long(plaintext)
        log.success("Found plaintext: {}".format(plaintext))
        for one_key in correct_keys:
            one_key.texts[0]['plain'] = plaintext
        return plaintext
    else:
        log.debug("Plaintext wasn't {}-th root")
        log.debug("result (from crt) = {}".format(e, result))
        log.debug("plaintext ({}-th root of result) = {}".format(e, plaintext))
        return False


def faulty(key, padding=None):
    """Faulty attack against crt-rsa, Boneh-DeMillo-Lipton
    sp = padding(m)**(d % p-1) % p
    sq' = padding(m)**(d % q-1) % q <--any error during computation
    s' = crt(sp, sq') % n <-- broken signature
    s = crt(sp, sq) % n <-- correct signature
    p = gcd(s'**e - u(m), n)
    p = gcd(s - s', n)

    Args:
        key(RSAKey): with at least one broken signature (key.texts[no]['cipher']) and corresponding
                     plaintext (key.texts[no]['plain']), or valid and broken signature
        padding(None/function): function used before signing message

    Returns:
        bool/RSAKey: False on failure, recovered private key otherwise
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
                log.debug("Found p={}".format(p))
                key = RSAKey.construct(key.n, key.e, p=long(p))
                return key

    log.debug("Check for valid-invalid signatures")
    signatures = [tmp['cipher'] for tmp in key.texts if 'cipher' in tmp]
    for pair in itertools.combinations(signatures, 2):
        p = gmpy2.gcd(pair[0] - pair[1], key.n)
        if p != 1 and p != key.n:
            log.debug("Found p={}".format(p))
            new_key = RSAKey.construct(key.n, key.e, p=long(p), identifier=key.identifier+'-private')
            new_key.texts = key.texts[:]
            return new_key
    return False


def parity_oracle(ciphertext):
    """Function implementing parity oracle

    Args:
        ciphertext(int)

    Returns:
        int: 0 (if decrypted ciphertext is even) or 1 (is odd)
    """
    raise NotImplementedError


def parity(parity_oracle, key):
    """Given oracle that returns LSB of decrypted ciphertext we can decrypt whole ciphertext
    parity_oracle function must be implemented

    Args:
        parity_oracle(function)
        key(RSAKey): contains ciphertexts to decrypt

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
            while lower_bound+1 < upper_bound:
                cipher = (two_encrypted * cipher) % key.n
                denominator *= 2
                numerator *= 2
                counter += 1

                is_odd = parity_oracle(cipher)
                if is_odd:  # plaintext > n/(2**counter)
                    numerator += 1
                lower_bound = (key.n * numerator) / denominator
                upper_bound = (key.n * (numerator+1)) / denominator

                log.debug("{} {} [{}, {}]".format(counter, is_odd, long(lower_bound), long(upper_bound)))
                log.debug("{}/{}  -  {}/{}\n".format(numerator, denominator, numerator+1, denominator))
            log.success("Decrypted: {}".format(i2b(upper_bound)))
            key.texts[text_no]['plain'] = upper_bound
            recovered[text_no] = upper_bound
    return recovered


def blinding(key, signing_oracle=None, decryption_oracle=None):
    """Perform signature/ciphertext blinding attack

    Args:
        key(RSAKey): with at least one plaintext(to sign) or ciphertext(to decrypt)
        signing_oracle(function)
        decryption_oracle(function)

    Returns:
        dict: keys: positions, values: signatures or plaintexts
        update key texts
    """
    if not signing_oracle and not decryption_oracle:
        log.critical_error("Give one of signing_oracle or decryption_oracle")
    if signing_oracle and decryption_oracle:
        log.critical_error("Give only one of signing_oracle or decryption_oracle")

    recovered = {}
    if signing_oracle:
        for text_no in range(len(key.texts)):
            if 'plain' in key.texts[text_no] and 'cipher' not in key.texts[text_no]:
                blind = random.randint(2, 100)
                blind = key.encrypt(blind)
                blinded_plaintext = (key.texts[text_no]['plain'] * blind) % key.n
                blinded_signature = signing_oracle(blinded_plaintext)
                if not blinded_signature:
                    log.critical_error("Error during call to signing_oracle({})".format(blinded_plaintext))
                signature = (invmod(blind, key.n) * blinded_signature ) % key.n
                key.texts[text_no]['cipher'] = signature
                recovered[text_no] = signature

    if decryption_oracle:
        for text_no in range(len(key.texts)):
            if 'cipher' in key.texts[text_no] and 'plain' not in key.texts[text_no]:
                blind = random.randint(2, 100)
                blind = key.encrypt(blind)
                blinded_ciphertext = (key.texts[text_no]['cipher'] * blind) % key.n
                blinded_plaintext = signing_oracle(blinded_ciphertext)
                if not blinded_plaintext:
                    log.critical_error("Error during call to decryption_oracle({})".format(blinded_plaintext))
                plaintext = (invmod(blind, key.n) * blinded_plaintext ) % key.n
                key.texts[text_no]['cipher'] = plaintext
                recovered[text_no] = plaintext

    return recovered
