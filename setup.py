from setuptools import setup, find_packages

setup(name='CryptoAttacks',
      version='0.1',
      description='Implementation of some cryptography attacks',
      url='https://github.com/GrosQuildu/CryptoAttacks',
      author='Gros Quildu',
      author_email='e2.8a.95@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      install_requires=['pycrypto', 'gmpy2', 'BeautifulSoup'])