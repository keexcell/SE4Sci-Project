import math

import pytest
from test_simple import check_tuple_close

from diffeqnsolver import EulerSolver, TaylorSolver


@pytest.mark.parametrize("solver_to_test", ["Euler", "Taylor"])
def test_separable(solver_to_test):
    """
    A first-order linear ODE,
    more complicated than the simple function,
    but still separable
    f(x,y) = y'(x) = 6x^2 - 3x^2y
    expect y(x) = 2 + Ce^{-x^3}
    """
    def f(x, y):
            return 6 * (x**2) - 3 * (x**2) * y
    
    num_steps = 5000
    x0 = 0
    y0 = 3
    # this makes C = 1
    xn = 10

    if solver_to_test == "Euler":
        y_prime = EulerSolver(f)
        rel_tol = 0.005
        y_prime.solve(x0, y0, xn, num_steps)
        y_prime.visualize("Euler", r"$6x^2 - 3x^2y$", r"$2+e^{-x^3}$")

    elif solver_to_test == "Taylor":
        y_prime = TaylorSolver(f)
        rel_tol = 0.005  # tolerance can be different between Taylor and Euler
        y_prime.solve(
            x0,
            y0,
            xn,
            num_steps,
            [
                lambda x, y: 12 * x - 6 * x * y - 18 * (x**4) + 9 * (x**4) * y,
                lambda x, y: 12
                - 6 * y
                - 6 * x * f(x, y)
                - 36 * (x**3)
                + 9 * (x**4) * f(x, y),
            ],
        )
        y_prime.visualize("Taylor", r"$6x^2 - 3x^2y$", r"$2+e^{-x^3}$")

    y_prime_solutionlist = y_prime.iterations

    for step in range(num_steps):
        x = ((xn - x0) / num_steps) * step
        y = 2 + math.exp(-(x**3))
        assert check_tuple_close(
            y_prime_solutionlist[step], (x, y, 6 * (x**2) - 3 * (x**2) * (y)), rel_tol
        )
