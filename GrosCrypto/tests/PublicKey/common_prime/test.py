#!/usr/bin/env python

from GrosCrypto.PublicKey.rsa import *
import os

keys = []
for key in os.listdir('.'):
    if key.endswith('.pem'):
        rsa = importKey(key)
        keys.append(rsa)

common_prime(keys)

