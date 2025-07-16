import math

import pytest

from diffeqnsolver import EulerSolver, TaylorSolver


def check_tuple_close(tuple1, tuple2, rel_tol):
    """
    Checks if the tuples are close, element-wise,
    tuple1[0] compared to tuple2[0] etc.
    Returns True if the tuples are close,
    Returns False if not.
    """
    for i in range(len(tuple1)):
        a = tuple1[i]
        b = tuple2[i]

        if not math.isclose(a, b, rel_tol=rel_tol, abs_tol=0.05):
            return False
    return True


def angle_maker(step, angle_length=2 * math.pi, num_steps=100):
    """
    Inputs
    ------
    step : int
        the number of the step at which you want the angle
    angle_length : float
        the difference between the start and ending x,
        called length because it's how far your list spans
    num_steps : int
        how many steps you are splitting the angle_length into
    Outputs
    -------
    angle : float
        the angle that occurs at the step number inputted
    """
    step_size = angle_length / num_steps
    angle = step * step_size
    return angle


@pytest.mark.parametrize("solver_to_test", ["Euler", "Taylor"])
def test_simple_trig(solver_to_test):
    """
    Just a simple f(x,y) = y'(x) = cos(x)
    Expect the answer to match y(x) = sin(x)
    x_0 = 0 means y(x_0) = y_0 = 0, go a full period to 2pi
    Each step will be about 0.0628 rad
    """
    num_steps = 5000

    if solver_to_test == "Euler":
        y_prime = EulerSolver(lambda x, y: math.cos(x))  # noqa: ARG005
        rel_tol = 0.005
        y_prime.solve(0.0, 0.0, 2 * math.pi, num_steps)
        y_prime_solutionlist = y_prime.iterations
        y_prime.visualize("Euler", "cos(x)")
    elif solver_to_test == "Taylor":
        y_prime = TaylorSolver(lambda x, y: math.cos(x))  # noqa: ARG005
        rel_tol = 0.005  # tol can be diff btwn Taylor and Euler
        y_prime.solve(
            0.0,
            0.0,
            2 * math.pi,
            num_steps,
            [lambda x, y: -math.sin(x), lambda x, y: -math.cos(x)],  # noqa: ARG005
        )
        y_prime_solutionlist = y_prime.iterations
        y_prime.visualize("Taylor", "cos(x)")

    assert type(y_prime_solutionlist[0]) is tuple
    assert type(y_prime_solutionlist[0][0]) is float

    for step in range(num_steps):
        angle = angle_maker(step, num_steps=num_steps)
        assert check_tuple_close(
            y_prime_solutionlist[step],
            (angle, math.sin(angle), math.cos(angle)),
            rel_tol,
        )
