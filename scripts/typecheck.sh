#!/usr/bin/env bash

set -e
set -u

git ls-files | grep '\.py' | xargs pyright
