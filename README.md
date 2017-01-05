# Cryptography attacks

### Requirements:
* Python 2.7
* gmpy2
* [pycrypto](https://pypi.python.org/pypi/pycrypto)

### Attacks:
* Classic
	+ [One time pad / xor](docs/Classic/one_time_pad.md)
		+ Guess key size
		+ Repeated key
		+ Reused key
* Block
	+ [CBC](docs/Block/cbc.md)
		+ Bit flipping
		+ Padding oracle
		* Key as IV
	+ [ECB](docs/Block/ecb.md)
		+ Byte-at-time decryption
* Public Key
	+ [RSA](docs/PublicKey/rsa.md)
	    * Small e, small plaintext
		+ Common primes
		+ Wiener's small private exponent
		+ Hastad's broadcast
		+ Faulty (RSA-CRT)
		+ Parity oracle
		* Blinding (signatures/ciphertexts)
		* Bleichenbacher'06 signature forgery
* [Hash](docs/Hash.md)
    * Length extension
* [Utils](docs/Utils.md)
* [Math](docs/Math.md)

For docs(strings) check docs/

For example uses check tests/

To change verbosity:
```python
from CryptoAttacks.Utils import log

log.level = 'debug'  # debug, info, success
```
