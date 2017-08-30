#!/usr/bin/env python

import os
import subprocess

from Block import test_ecb
from Block import test_cbc
from PublicKey import test_rsa
import test_Hash

SAGE_TESTS = True

os.chdir('./Block/')
test_ecb.run()
test_cbc.run()
if SAGE_TESTS:
    print(subprocess.check_output(["sage", "./test_whitebox_aes.sage"]))

os.chdir('../PublicKey/')
test_rsa.run()

os.chdir('../')
test_Hash.run()

os.chdir('../EllipticCurve')
if SAGE_TESTS:
    print(subprocess.check_output(["sage", "./test_ecdsa.sage"]))