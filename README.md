# Pyster

Pyster is a coverage-driven automatic unit test generator for Python projects.

## Pre-request
Pyster works well with Python 3.7 or above. Python 3.6 would raise error in static analysis stage. 
```bash
$ python3 --version
Python 3.7.5
```

## Usage
```bash
python3 -m src.pyster <path-to-python-file>
```

```
usage: pyster [-h] [--timeout timeout] [--coverage coverage_target] path

Generate Unit Tests

positional arguments:
  path                  the path to source files

optional arguments:
  -h, --help            show this help message and exit
  --timeout timeout     user defined time limit for the program to run in
                        seconds
  --coverage coverage_target
                        target coverage for the generated tests in percentage
```

## Test on existing samples
```bash
git submodule update --init --recursive
cd samples
./applyPatch.sh
```

## Sample execution
```bash
# Phase 1
python3 -m src.pyster.init --project_path samples --module_name foobar.foobar
# Phase 2
python3 -m src.pyster.gen --project_path samples --module_name foobar.foobar
```


## Concept
* Use built-in Python functions to obtain all methods in a Python class.
* According to the methods input, randomly generate an object instance and function arguments, with special inputs (`0`, `-1` for integers, `[]` for lists and `None` for objects also into consideration). Use `coverage.py` third-party library to get the coverage rate increment after calling the randomly generated function call.
* Repeat step 2 until we reached 100% coverage rate or the target coverage rate from user input, or the specified timeout is reached.
* Dump all auto-generated unit tests into a test file and save it into the project test suite directory, together with a before/after coverage rate of the class.
