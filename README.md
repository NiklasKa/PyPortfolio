# PyPortfolio: My personal Python Portfolio
The projects inside my python portfolio are build during [**100 Days of Code: The Complete Python Pro Bootcamp for 2022**](https://www.udemy.com/course/100-days-of-code/) by [**Dr. Angela Yu**](https://github.com/angelabauer).

## Installation
Create conda environment
```shell
conda env create -f environment.yml
```

Activate environment and install library
```shell
conda activate pyPortfolio
pip install -e .
```

## Projects
### pyMorse
[![Generic badge](https://img.shields.io/badge/-Scripting-blue.svg)](https://github.com/NiklasKa/PyPortfolio)

A text-based Python program to convert Strings into Morse Code.

```python
from pyMorse.utils import encode
print(encode("SOS"))
```
