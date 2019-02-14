#!/bin/bash

find . -name '*.sage' -not -path '*/tests/*' -exec sage --preparse {} \; -exec sh -c 'mv "$1.py" "${1%.sage}_sage.py"' _ {}  \;