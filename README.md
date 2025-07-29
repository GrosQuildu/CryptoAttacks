# Cryptography attacks

Archived. Scripts should work, but I'm not planning to refactor or add new attacks.

### Requirements:
* Python 2.7 or 3.7
* future
* [pycrypto](https://pypi.python.org/pypi/pycrypto)
* gmpy2
* BeautifulSoup4
* requests
* termcolor

### Installation:
```
git clone https://github.com/GrosQuildu/CryptoAttacks
cd CryptoAttacks
python ./setup.py install
```

### Attacks:
(* means Sage script)
* Classic
	+ [One time pad / xor](CryptoAttacks/docs/Classic/one_time_pad.md)
		+ Guess key size
		+ Repeated key
		+ Reused key
* Block
	+ [CBC](CryptoAttacks/docs/Block/cbc.md)
		+ Bit flipping
		+ Padding oracle
		    + Decrypt ciphertext
		    + Forge ciphertext that will decrypt to given plaintext
		+ Key as IV
	+ [ECB](CryptoAttacks/docs/Block/ecb.md)
		+ Byte-at-time decryption
		+ Known plaintexts
	+ [GCM](CryptoAttacks/docs/Block/gcm.md)
		+ auth key recovery with biased nonce
    + [Whitebox AES](CryptoAttacks/docs/Block/whitebox_aes.md)
	    + Differential fault analysis*
* Public Key
	+ [RSA](CryptoAttacks/docs/PublicKey/rsa.md)
	    + Small e, small plaintext
		+ Common primes
		+ Wiener's small private exponent
		+ Hastad's broadcast
		+ Faulty (RSA-CRT)
		+ Parity oracle
		+ Blinding (signatures/ciphertexts)
		+ Bleichenbacher'06 signature forgery
		+ Duplicate-Signature Key Selection
        + Bleichenbacher's PKCS1.5 oracle 
        + Manger's OAEP oracle
* Elliptic Curves
    + [ECDSA](CryptoAttacks/docs/EllipticCurve/ecdsa.md)
        + Biased nonce (LSB equals to zero)*
        + Duplicate-Signature Key Selection*
    + Pohlig-Hellman*
    + [Discrete log on singular curves\*](CryptoAttacks/docs/EllipticCurve/singular.md)
    + [Invalid curves attack](CryptoAttacks/docs/EllipticCurve/invalid_curves.md)
* [Hash](CryptoAttacks/docs/Hash.md)
    * Length extension (sha1, md4)
* [PRNG](CryptoAttacks/docs/PRNG.md)
	* Linear Congruence generator
* [Utils](CryptoAttacks/docs/Utils.md)
* [Math](CryptoAttacks/docs/Math.md)

For docs(strings) check CryptoAttacks/docs/

For example uses check CryptoAttacks/tests/

To change verbosity:
```python
from CryptoAttacks.Utils import log

log.level = 'debug'  # debug, info, success
```

Most functions takes and returns bytes (not str), to use with python2 do:
```python
from builtings import bytes

arg = bytes(b'some arg')
```
