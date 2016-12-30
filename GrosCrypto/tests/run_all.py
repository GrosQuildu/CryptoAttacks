#!/usr/bin/env python

import os
from Block import ecb
from Block import cbc
from PublicKey import rsa

os.chdir('./Block/')
ecb.run()
cbc.run()

os.chdir('../PublicKey/')
rsa.run()