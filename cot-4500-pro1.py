import math
from sympy import symbols
import sympy as sym


def f(x):
    return x**3 + 4 * x**2 - 10


def g(x):
    return math.sqrt((10 - x**3) / 4)


def bisection_method(a, b, tol=1e-4, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Bisection method fails - function has same sign at endpoints")
        return None

    iter_count = 0
    while (b - a) >= tol and iter_count < max_iter:
        c = (a + b) / 2
        print(f"Bisection - Iteration {iter_count}: x = {c:.6f}")

        if abs(f(c)) < tol:
            print(
                f"Bisection - Root found at x = {c:.6f} after {iter_count} iterations"
            )
            return c

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1

    root = (a + b) / 2
    print(
        f"Bisection - Root found at x = {root:.6f} after {iter_count} iterations"
    )
    return root


def fixed_point_iteration(p0=1.5, tol=1e-7, max_iter=100):
    print(f"Fixed Point - Iteration 0: x = {p0}")

    for i in range(1, max_iter + 1):
        p = g(p0)

        if math.isnan(p):
            print("Fixed Point - Divergence detected")
            return None

        print(f"Fixed Point - Iteration {i}: x = {p:.8f}")

        if abs(p - p0) < tol:
            print(f"Fixed Point - Converged to {p:.8f} after {i} iterations")
            return p

        p0 = p

    print(f"Fixed Point - Failed to converge after {max_iter} iterations")
    return None


def newton_method(x0, tol=1e-4, max_iter=100):
    x = symbols('x')
    equation = x**3 + 4 * x**2 - 10
    derivative = sym.diff(equation, x)

    x_val = x0
    for i in range(max_iter):
        fx = equation.subs('x', x_val)
        fx_prime = derivative.subs('x', x_val)

        if abs(fx) < tol:
            print(
                f"Newton - Root found at x = {x_val:.6f} after {i+1} iterations"
            )
            return x_val

        if fx_prime == 0:
            print("Newton - Derivative is zero. Method fails.")
            return None

        x_new = x_val - fx / fx_prime
        print(f"Newton - Iteration {i+1}: x = {x_new:.6f}")

        if abs(x_new - x_val) < tol:
            print(
                f"Newton - Root found at x = {x_new:.6f} after {i+1} iterations"
            )
            return x_new

        x_val = x_new

    print("Newton - Maximum iterations reached without convergence")
    return x_val


def sqrt_approximation(x0=1.5, tol=1e-6, max_iter=100):
    iter_count = 0
    diff = float('inf')
    x = x0

    print(f"Sqrt Approximation - Iteration {iter_count}: {x}")

    while diff >= tol and iter_count < max_iter:
        iter_count += 1
        y = x
        x = (x / 2) + (1 / x)
        print(f"Sqrt Approximation - Iteration {iter_count}: {x}")
        diff = abs(x - y)

    print(f"Sqrt Approximation - Convergence after {iter_count} iterations")
    return x


def main():
    # Initial parameters
    a, b = -4, 7  # Endpoints for bisection
    x0 = 1.5  # Initial guess for other methods

    print("\n=== Bisection Method ===")
    bisection_root = bisection_method(a, b)

    print("\n=== Fixed Point Iteration ===")
    fp_root = fixed_point_iteration(x0)

    print("\n=== Newton's Method ===")
    newton_root = newton_method(x0)

    print("\n=== Square Root Approximation ===")
    sqrt_root = sqrt_approximation(x0)

    print("\n=== Final Results ===")
    print(f"Bisection Method: {bisection_root:.6f}")
    print(f"Fixed Point: {fp_root:.6f}" if fp_root else "Fixed Point: Failed")
    print(f"Newton's Method: {newton_root:.6f}"
          if newton_root else "Newton's: Failed")
    print(f"Sqrt Approximation: {sqrt_root:.6f}")


if __name__ == "__main__":
    main()
