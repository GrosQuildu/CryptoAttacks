#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import subprocess

from Block import test_ecb
from Block import test_cbc
from PublicKey import test_rsa
import test_Hash

SAGE_TESTS = True

print("TEST BLOCK CIPHERS")
os.chdir('./Block/')

print("Test ecb")
test_ecb.run()

print("\nTest cbc")
test_cbc.run()

print("\nTest whitebox aes")
if SAGE_TESTS:
    subprocess.call(["sage", "./test_whitebox_aes.sage"])
print("\n")
# --------------------------------------------------

print("TEST PUBLIC KEY")
os.chdir('../PublicKey/')
print("Test rsa")
test_rsa.run()
print("\n")
# --------------------------------------------------

print("TEST HASH")
os.chdir('../')
test_Hash.run()
print("\n")
# --------------------------------------------------

print("TEST ELLIPTIC CURVES")
os.chdir('./EllipticCurve')
if SAGE_TESTS:
    subprocess.call(["sage", "./test_ecdsa.sage"])