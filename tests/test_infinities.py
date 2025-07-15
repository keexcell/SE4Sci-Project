from diffeqnsolver import Solver, EulerSolver, TaylorSolver
from test_simple import check_tuple_close, angle_maker
import pytest
import math
import abc


#@pytest.mark.parametrize('solver_to_test', ['Euler', 'Taylor'])
#def test_divergence(solver_to_test):
def test_divergence():
    '''
    Now trying 2 variables, still simpler: f(x,y) = y'(x) = y*tan(x)
    Expect the answer to match y(x) = 1/cos(x)
    x_0 = 0 means y(x_0) = y_0 = 1, go a full period to 2pi
    Do 500 steps so each step will be about 0.0126 rad

    Has a discontinuity at pi/2 and 3pi/2, 
    but it might work on closed intervals
    '''
    num_steps = 500

#    if solver_to_test == 'Euler':
    tol = 0.1
    y_prime = EulerSolver(lambda x, y : y*math.tan(x))
#    elif solver_to_test == 'Taylor':
#        y_prime = TaylorSolver(lambda x, y : y*math.tan(x))
        #rel_tol = 1e-9
        #abs_tol = 1e-4
    
    #there's cases where cos = 0 so y = 1/0 and there will be an error
    with pytest.raises(ValueError):
        y_prime.solve(0.0, 1.0, 2*math.pi, num_steps)
        
    #test if it overwrites first .solve with another. this time closed interval
    y_prime.solve(0.0, 1.0, math.pi/3, num_steps)
    y_prime_solutionlist = y_prime.iterations
    assert math.isclose(y_prime_solutionlist[-1][0], math.pi/3)

    for step in range(num_steps):
        angle = angle_maker(step, angle_length = math.pi/3, num_steps = num_steps)
        assert check_tuple_close(y_prime_solutionlist[step], 
                                (angle, 1/math.cos(angle), math.tan(angle)/math.cos(angle)), tol)
    
    