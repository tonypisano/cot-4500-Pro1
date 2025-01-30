
# Root Finding Methods Implementation

This project implements various numerical methods for finding roots of equations, specifically solving x³ + 4x² - 10 = 0.

## Methods Implemented

1. **Bisection Method**
   - Uses interval halving to find roots
   - Requires initial interval [a,b] where f(a) and f(b) have opposite signs

2. **Fixed Point Iteration**
   - Based on converting equation to x = g(x) form
   - Requires good initial guess
   - May diverge if |g'(x)| > 1

3. **Newton's Method**
   - Uses tangent lines to approximate roots
   - Fastest convergence when close to root
   - May fail if derivative becomes zero

4. **Square Root Approximation**
   - Special method for finding √2

## Usage

1. Run the main program:
```bash
python cot-4500-pro1.py
```

2. Run individual methods:
```bash
python bisection.py #bisection   
python fp_method.py #Fixed Point   
python newton.py  #newton  
python approx.py  #approximation     
```

## Parameters

- Default tolerance: 1e-4 to 1e-7
- Maximum iterations: 0
- Initial interval for bisection: [-4, 7]
- Initial guess for other methods: 1.5

## Dependencies

- Python 3.11+
- SymPy library for symbolic mathematics

## Output Format

Each method displays:
- Iteration number
- Current approximation
- Final root value
- Number of iterations taken
- Convergence status

## Error Handling

The program handles:
- Invalid intervals
- Divergence
- Zero derivatives
- Maximum iteration limits
