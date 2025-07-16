from diffeqnsolver import Solver, EulerSolver, TaylorSolver
from test_simple import check_tuple_close, angle_maker
import pytest
import math
import abc


@pytest.mark.parametrize('solver_to_test', ['Euler', 'Taylor'])
def test_linear(solver_to_test):
    '''
    A first-order linear ODE, 
    more complicated than the simple function,
    but still separable
    f(x,y) = y'(x) = 6x^2 - 3x^2y
    expect y(x) = 2 + Ce^{-x^3}
    '''
    num_steps = 5000

    if solver_to_test == 'Euler':
        y_prime = EulerSolver(lambda x, y : 6*(x**2) - 3*(x**2)*(y))
        rel_tol = 0.005
    elif solver_to_test == 'Taylor':
        y_prime = TaylorSolver(lambda x, y : 6*(x**2) - 3*(x**2)*(y))
        rel_tol = 0.005 #tolerance can be different between Taylor and Euler

    x0 = 0
    y0 = 3
    #this makes C = 1
    xn = 10
    y_prime.solve(x0, y0, xn, num_steps)
    y_prime_solutionlist = y_prime.iterations

    for step in range(num_steps):
        x = ((xn - x0)/num_steps)*step
        y = 2 + math.exp(-x**3)
        assert check_tuple_close(y_prime_solutionlist[step], (x, y, 6*(x**2) - 3*(x**2)*(y)), rel_tol)

'''
@pytest.mark.parametrize('solver_to_test', ['Euler', 'Taylor'])
def test_nonlinear(solver_to_test):
    '''
    A first-order nonlinear ODE,
    form of the Bernoulli equation
    f(x,y) = y'(x) = xy^2 - x^2y
    expect y(x) = C/(1+e^(x^2/2))
    '''
    num_steps = 5000

    if solver_to_test == 'Euler':
        y_prime = EulerSolver(lambda x, y : (x)*(y**2) - (x**2)*(y))
        rel_tol = 0.005
    elif solver_to_test == 'Taylor':
        y_prime = TaylorSolver(lambda x, y : (x)*(y**2) - (x**2)*(y))
        rel_tol = 0.005 #tolerance can be different between Taylor and Euler

    x0 = 0
    y0 = 3
    #this makes C = 1
    xn = 10
    y_prime.solve(x0, y0, xn, num_steps)
    y_prime_solutionlist = y_prime.iterations

    for step in range(num_steps):
        x = ((xn - x0)/num_steps)*step
        y = 2 + math.exp(-x**3)
        assert check_tuple_close(y_prime_solutionlist[step], (x, y, 6*(x**2) - 3*(x**2)*(y)), rel_tol)
'''
