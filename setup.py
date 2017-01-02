from setuptools import setup

setup(name='CryptoAttacks',
      version='0.1',
      description='Implementation of some cryptography attacks',
      url='https://github.com/GrosQuildu/CryptoAttacks',
      author='Gros Quildu',
      author_email='e2.8a.95@gmail.com',
      license='MIT',
      packages=['CryptoAttacks'],
      zip_safe=False,
      install_requires=['pycrypto', 'gmpy2'])