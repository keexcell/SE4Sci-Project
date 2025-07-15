from diffeqnsolver import Solver, EulerSolver, TaylorSolver
import pytest
import math
import abc

def check_tuple_close(tuple1, tuple2, tol):
    '''
    Checks if the tuples are close, element-wise, 
    tuple1[0] compared to tuple2[0] etc.
    Returns True if the tuples are close, 
    Returns False if not.
    '''
    for i in range(len(tuple1)):
        a = tuple1[i]
        b = tuple2[i]
        should_be_0 = a - b
        
        average = (a + b) / 2
        if average == 0:
            return "Error: Cannot calculate percentage difference because the average of the two values is zero."
        difference = abs(a - b)
        percent_diff = (difference / average) * 100        
        if not should_be_0 == pytest.approx(0, abs=tol):
            print('Values: {} and {}  Percent Difference = {}'.format(a, b, percent_diff))
            return False
    return True


def angle_maker(step, angle_length = 2*math.pi, num_steps = 100):
    '''
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
    '''
    step_size = angle_length / num_steps
    angle = step * step_size 
    return angle

#@pytest.mark.parametrize('solver_to_test', ['Euler', 'Taylor'])
#def test_simple_trig(solver_to_test):
def test_simple_trig():
    '''
    Just a simple f(x,y) = y'(x) = cos(x) 
    Expect the answer to match y(x) = sin(x)
    x_0 = 0 means y(x_0) = y_0 = 0, go a full period to 2pi
    Each step will be about 0.0628 rad 
    '''
    num_steps = 500
#    if solver_to_test == 'Euler':
    tol = 0.05 #idk what this should be
    y_prime = EulerSolver(lambda x, y : math.cos(x))
#    elif solver_to_test == 'Taylor':
#        y_prime = TaylorSolver(lambda x, y : math.cos(x))
        #tol = 0.01
    y_prime.solve(0.0, 0.0, 2*math.pi, num_steps)
    y_prime_solutionlist = y_prime.iterations

    for num in range(num_steps):
        angle = angle_maker(num, num_steps = num_steps)
        assert check_tuple_close(y_prime_solutionlist[num], (angle, math.sin(angle), math.cos(angle)), tol)
