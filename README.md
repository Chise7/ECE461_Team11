# ECE 30861: A CLI for trustworthy module re-use

### Team members

- Philip Chu
- Esteban Gorostiaga
- Connor Hise
- Kevin Kwon

### Directory structure

## Basic Use

Install dependencies

    ./run install

Create binary executable

    ./run build

Run the CLI program

    ./run <URL_FILE>

`URL_FILE` is a URLs separated by newlines.

Run the full test suite

    ./run test

## Miscellaneous

Clean up products of compilation

    make clean

View lines of code by language (see [AlDanial/cloc](https://github.com/AlDanial/cloc))

    make cloc
