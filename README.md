# Dictppr

[![Release](https://img.shields.io/github/v/release/TheFifthLeaf/dictppr?color=3C7DD9)](https://github.com/TheFifthLeaf/dictppr/releases)
[![Min. Python version](https://img.shields.io/badge/python-3.6%2B-3C7DD9)](https://www.python.org/downloads/)
[![License GPLv3](https://img.shields.io/badge/license-GPL%20V3-3C7DD9)](https://choosealicense.com/licenses/gpl-3.0/)
[![Code quality](https://img.shields.io/codefactor/grade/github/TheFifthLeaf/dictppr/main?color=3C7DD9)](https://www.codefactor.io/repository/github/thefifthleaf/dictppr)
[![Tests](https://github.com/TheFifthLeaf/dictppr/actions/workflows/tests.yml/badge.svg)](https://github.com/TheFifthLeaf/dictppr/actions/workflows/tests.yml)

A package that allows easy-to-read conversion
of a dictionary to a string and pretty printing.

Features
- Convert dictionary to string
- Convert dictionary to dictionary of string
- Pretty print dictionary

## Installation
Download the latest version from `PyPi`
```bash
python -m pip install dictppr
```
Developers should also install tests dependencies
```bash
pip install -r requirements_dev.txt
```

## Testing
Perform the tests with `pytest` (or `Tox`)
```bash
python -m pytest tests
```
To check test coverage
```bash
coverage report -m
```

Current coverage:
| Name                     | Stmts | Miss | Cover |
|:-------------------------|------:|-----:|------:|
| dictppr\\\_\_init\_\_.py | 3     | 0    | 100%  |
| dictppr\dictppr.py       | 68    | 1    | 99%   |

## Usage
First, you need to import the package:
```python
import dictppr
```
Now, to get string from dictionary:
```python
string = dictppr.get({...})
```
..or to get dictionary of strings:
```python
dictionary = dictppr.convert({...})
```
..or you just want to print it:
```python
dictppr.pprint({...})
```
If you need to check version of dictppr, use:
```python
print(dictppr.__version__)
```
### Examples
You have dictionary like that:
```python
sample = {
    "key_1": "val_1",
    "key_2": {
        "key_3": "val_3",
        "key_4": "val_4"
    }
}
```
You will get this string with the `get` function:
```python
string = "key_1:val_1, key_2:key_3:val_3, key_4:val_4"
```
You will get this dictionary with the `convert` function:
```python
dictionary = {"key_1": "val_1", "key_2": "key_3:val_3, key_4:val_4"}
```
You will get this stdout with the `pprint` function:
```text
key_1 => val_1
key_2 => key_3:val_3, key_4:val_4
```

## Contributing
Pull requests are welcome!
