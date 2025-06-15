#!/usr/bin/env bash
set -o errexit
typst compile --root . paper/paper.typ paper.pdf
