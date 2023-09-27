#!/usr/bin/env sh

set -ex

# clean up
coverage erase
rm -rf htmlcov

# generate coverage
coverage run -m unittest discover
coverage report
coverage html
#coverage-badge -fo coverage.svg

# serve files
python -m http.server 4242 -d htmlcov
