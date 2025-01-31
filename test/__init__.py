import subprocess

subprocess.call(["git", "pull"])
subprocess.call(["make"])
subprocess.call(["make", "test"])
from sympy import symbols
import sympy as sym
import math
