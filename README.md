# fstring
[![Build Status](https://travis-ci.org/rinslow/fstring.svg?branch=master)](https://travis-ci.org/rinslow/fstring)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fstring.svg)
[![PyPI version](https://badge.fury.io/py/fstring.svg)](https://badge.fury.io/py/fstring)

Alows easy python usage of strings.

## Usage
```pip install fstring```

```python
from fstring import fstring
x = 1
y = 2.0
plus_result = "3.0"
print fstring("{x}+{y}={plus_result}")  # Prints: 1+2.0=3.0
```
Also supports evaluation
```python
print fstring("1+1 is {1+1}")
```


Now you don't need to format your strings with %s %r or %d, or even number them by order of appearance.
you can just call them by their name which makes your code so so so much more readable!

instead of ```print "Hello, %s :) What a nice %s?" % (username, time_of_day)```

how about ```print fstring("Hello {username} :), What a nice {time_of_day}?")```?

