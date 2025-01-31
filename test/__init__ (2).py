from sympy import symbols
import sympy as sym
import math

#functions
from .bisection import bisection_method, f as bisection_f
from .newton import newton_method
from .fp_method import fixed_point_iteration, g
from .approx import main as sqrt_approximation

#constants
DEFAULT_TOLERANCE = 1e-4
MAX_ITERATIONS = 100
INITIAL_GUESS = 1.5
INTERVAL = (-4, 7)  #interval [a, b]

#common equations
x = symbols('x')
DEFAULT_EQUATION = x**3 + 4*x**2 - 10

# Packages
__version__ = '0.1.0'
__author__ = 'Your Name'
__email__ = 'your.email@example.com'
__all__ = [
    'bisection_method',
    'newton_method',
    'fixed_point_iteration',
    'sqrt_approximation',
    'DEFAULT_TOLERANCE',
    'MAX_ITERATIONS',
    'INITIAL_GUESS',
    'INTERVAL',
    'DEFAULT_EQUATION',
    'bisection_f',
    'g'
]

# Initialize package-wide settings
def setup(tolerance=DEFAULT_TOLERANCE, max_iter=MAX_ITERATIONS):
    global DEFAULT_TOLERANCE, MAX_ITERATIONS
    DEFAULT_TOLERANCE = tolerance
    MAX_ITERATIONS = max_iter
