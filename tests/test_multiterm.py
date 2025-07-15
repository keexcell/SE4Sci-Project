from diffeqnsolver import Solver, EulerSolver, TaylorSolver
from test_simple import check_tuple_close, angle_maker
import pytest
import math
import abc


#@pytest.mark.parametrize('solver_to_test', ['Euler', 'Taylor'])
#def test_separable(solver_to_test):
def test_separable():
    '''
    A first-order linear ODE, 
    more complicated than the simple function,
    but still separable
    f(x,y) = y'(x) = 6x^2 - 3x^2y
    expect y(x) = 2 + Ce^{-x^3}
    '''
    num_steps = 5000
    rel_tol = 0.005 #more steps, less tolerant

    #if solver_to_test == 'Euler':
    y_prime = EulerSolver(lambda x, y : 6*(x**2) - 3*(x**2)*(y))
    #elif solver_to_test == 'Taylor':
        #y_prime = TaylorSolver(lambda x, y : 6*(x**2) - 3*(x**2)*(y))
        #rel_tol = 0.01
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

    y_prime.visualize("Euler")


#@pytest.mark.parametrize('solver_to_test', ['Euler', 'Taylor'])
#def test_separable(solver_to_test):
def test_separable():
    '''
    A first-order linear ODE, 
    more complicated than the simple function,
    but still separable
    f(x,y) = y'(x) = 6x^2 - 3x^2y
    expect y(x) = 2 + Ce^{-x^3}
    '''
    num_steps = 5000
    rel_tol = 0.005 #more steps, less tolerant

    #if solver_to_test == 'Euler':
    y_prime = EulerSolver(lambda x, y : 6*(x**2) - 3*(x**2)*(y))
    #elif solver_to_test == 'Taylor':
        #y_prime = TaylorSolver(lambda x, y : 6*(x**2) - 3*(x**2)*(y))
        #rel_tol = 0.01
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

    y_prime.visualize("Euler", "$6x^2 - 3yx^2$")

