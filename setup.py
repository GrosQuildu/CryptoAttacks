from distutils.command.build_py import build_py as _build_py
from distutils.core import setup
from subprocess import call

from setuptools import find_packages, setup


class build_py(_build_py):
    """Preparse and rename to .py all sage files to make them importable"""
    print("Preparsing sage files")
    call(['bash', './preparse_sage.bash'])

setup(name='CryptoAttacks',
        version='0.1',
        description='Implementation of some cryptography attacks',
        url='https://github.com/GrosQuildu/CryptoAttacks',
        author='Gros Quildu',
        author_email='e2.8a.95@gmail.com',
        license='MIT',
        packages=find_packages(),
        zip_safe=False,
        cmdclass={'build_py': build_py},
        install_requires=('future', 'pycrypto', 'gmpy2', 'BeautifulSoup4', 'requests', 'termcolor'),
        classifiers=('Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3',
                     'License :: OSI Approved :: MIT License')
)
