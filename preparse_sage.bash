#!/bin/bash

find . -name '*.sage' -exec sage --preparse {} \; -exec sh -c 'mv "$1.py" "${1%.sage}.py"' _ {}  \;