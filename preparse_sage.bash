#!/bin/bash

find . -name '*.sage' -path ./tests -prune -o -exec sage --preparse {} \; -exec sh -c 'mv "$1.py" "${1%.sage}_sage.py"' _ {}  \;