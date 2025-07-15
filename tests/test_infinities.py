from diffeqnsolver import Solver, EulerSolver, TaylorSolver
from test_simple import check_tuple_close, angle_maker
import pytest
import math
import abc
import matplotlib.pyplot as plt


def check_tuple_far(tuple1, tuple2):
    for i in range(len(tuple1)):
        if not math.isclose(tuple1[i], tuple2[i]):
            return True
        else:
            return False

def angle_maker(step, angle_length = 2*math.pi, num_steps = 100):
    step_size = angle_length / num_steps
    angle = step * step_size
    return angle

def test_divergence():
    '''
    Now trying 2 variables, still simpler: f(x,y) = y'(x) = y*tan(x)
    Expect the answer to match y(x) = 1/cos(x)
    x_0 = 0 means y(x_0) = y_0 = 1
    First, go a full period to 2pi
    Has a discontinuity at pi/2 and 3pi/2, 
    Second, just go to pi/3 so its a closed interval
    '''
    num_steps = 5000
    rel_tol = 0.005

    #if solver_to_test == 'Euler':
    y_prime = EulerSolver(lambda x, y : y*math.tan(x))
    #elif solver_to_test == 'Taylor':
        #y_prime = TaylorSolver(lambda x, y : y*math.tan(x))
        #rel_tol = 1e-9
    
    #there's cases where cos = 0 so y = 1/0 and there will be an error
    with pytest.raises(ValueError):
        y_prime.solve(0.0, 1.0, 2*math.pi, num_steps)
        
    #test if it overwrites first .solve with another. this time closed interval
    y_prime.solve(0.0, 1.0, math.pi/3, num_steps)
    y_prime_solutionlist = y_prime.iterations
    assert math.isclose(y_prime_solutionlist[-1][0], math.pi/3)

    y_prime.visualize("Eueler", "ytan(x)")

    for step in range(num_steps):
        angle = angle_maker(step, angle_length = math.pi/3, num_steps = num_steps)
        assert check_tuple_close(y_prime_solutionlist[step], 
                                (angle, 1/math.cos(angle), math.tan(angle)/math.cos(angle)), rel_tol)
    
    
