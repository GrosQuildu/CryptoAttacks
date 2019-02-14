#!/usr/bin/env python

from __future__ import absolute_import, division, print_function

import os
import subprocess
from os.path import abspath, dirname
from os.path import join as join_path

import test_Hash
from Block import test_cbc, test_ecb
from PublicKey import test_rsa

SAGE_TESTS = True
current_path = dirname(abspath(__file__))

print("TEST BLOCK CIPHERS")
print("Test ecb")
test_ecb.run()

print("\nTest cbc")
test_cbc.run()

print("\nTest whitebox aes")
if SAGE_TESTS:
    subprocess.call(["sage", join_path(current_path, "Block/test_whitebox_aes.sage")])
print("\n")
# --------------------------------------------------

print("TEST PUBLIC KEY")
print("Test rsa")
test_rsa.run()
print("\n")
# --------------------------------------------------

print("TEST HASH")
test_Hash.run()
print("\n")
# --------------------------------------------------

print("TEST ELLIPTIC CURVES")
if SAGE_TESTS:
    subprocess.call(["sage", join_path(current_path, "EllipticCurve/test_ecdsa.sage")])
