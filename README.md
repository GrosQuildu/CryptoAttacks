
# Cryptography attacks

### requirements:
* Python 2.7
* [pycrypto](https://pypi.python.org/pypi/pycrypto)

### attacks:
* Classic
	+ One time pad / xor
		+ Guess key size
		+ Repeated key
		+ Reused key
* Block
	+ CBC
		+ Bit flipping
		+ Padding oracle
	+ ECB
		+ Byte-at-time decryption
*Public Key
	+ RSA
		+ Common primes
		+ Wiener's small private exponent
		+ Hastad's broadcast
		+ Faulty (RSA-CRT)
		+ Parity oracle