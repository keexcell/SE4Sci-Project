from diffeqnsolver import Solver, EulerSolver
import pytest
import math
import abc
import matplotlib.pyplot as plt

def check_tuple_close(tuple1, tuple2):
    for i in range(len(tuple1)):
        if not math.isclose(tuple1[i], tuple2[i]):
            return False
        else:
            return True

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

def test_simple_trig():
    '''
    Just a simple f(x,y) = y'(x) = cos(x) 
    Expect the answer to match y(x) = sin(x)
    x_0 = 0 means y(x_0) = y_0 = 0, go a full period to 2pi
    Each step will be about 0.0628 rad
    '''

    y_prime = EulerSolver(lambda x, y : math.cos(x))
    y_prime.solve(0.0, 0.0, 2*math.pi)
    y_prime_solutionlist = y_prime.iterations

    angle_at_step35 = angle_maker(35)
    angle_at_step52 = angle_maker(52)
    angle_at_step71 = angle_maker(71)

    assert check_tuple_close(y_prime_solutionlist[0], (0.0, 0.0, 1.0))
    assert check_tuple_close(y_prime_solutionlist[-1], (2*math.pi, 0.0, 1.0))
    assert check_tuple_close(y_prime_solutionlist[35], (angle_at_step35, math.sin(angle_at_step35), math.cos(angle_at_step35)))
    assert check_tuple_close(y_prime_solutionlist[52], (angle_at_step52, math.sin(angle_at_step52), math.cos(angle_at_step52)))
    assert check_tuple_close(y_prime_solutionlist[71], (angle_at_step71, math.sin(angle_at_step71), math.cos(angle_at_step71)))

    assert check_tuple_far(y_prime_solutionlist[0], (angle_at_step52, math.sin(angle_at_step52), math.cos(angle_at_step52)))

    y_prime.visualize("Eueler")


def test_twovar_trig():
@pytest.mark.parametrize('solver_to_test', ['Euler', 'Taylor'])
def test_twovars(solver_to_test):
    '''
    Now trying 2 variables, still simpler: f(x,y) = y'(x) = y*tan(x)
    Expect the answer to match y(x) = 1/cos(x)
    x_0 = 0 means y(x_0) = y_0 = 1, go a full period to 2pi
    Do 500 steps so each step will be about 0.0126 rad

    Has a discontinuity at pi/2 and 3pi/2
    '''

    step_size = 2*math.pi / 500
    step2 = int((3*math.pi/2) / step_size)
    print(step2)

    if solver_to_test == 'Euler':
        y_prime = EulerSolver(lambda x, y : y*math.tan(x))
    elif solver_to_test == 'Taylor':
        y_prime = TaylorSolver(lambda x, y : y*math.tan(x))
    y_prime.solve(0.0, 1.0, 2*math.pi, 500)
    y_prime_solutionlist = y_prime.iterations

    y_prime.visualize("Eueler")

    angle_at_step35 = angle_maker(35, num_steps = 500)
    angle_at_step252 = angle_maker(252, num_steps = 500)
    angle_at_step171 = angle_maker(171, num_steps = 500)

    #whole bunch of checking values:
    assert check_tuple_close(y_prime_solutionlist[0], (0.0, 1.0, 0.0))
    assert check_tuple_close(y_prime_solutionlist[-1], (2*math.pi, 1.0, 0.0))
    assert check_tuple_close(y_prime_solutionlist[35], (angle_at_step35, 1/math.cos(angle_at_step35), math.tan(angle_at_step35)/math.cos(angle_at_step35)))
    assert check_tuple_close(y_prime_solutionlist[252], (angle_at_step252, 1/math.cos(angle_at_step252), math.cos(angle_at_step252)/math.cos(angle_at_step252)))
    assert check_tuple_close(y_prime_solutionlist[171], (angle_at_step171, 1/math.cos(angle_at_step171), math.cos(angle_at_step171)/math.cos(angle_at_step171)))
    assert check_tuple_far(y_prime_solutionlist[0], (angle_at_step252, 1/math.cos(angle_at_step252), math.cos(angle_at_step252)/math.cos(angle_at_step252)))

    #there's cases where cos = 0 so y = 1/0 and there will be an error. let's figure out what happens there
    step_size = 2*math.pi / 500
    step1 = int((math.pi/2) / step_size)+1 #zeroindexing
    step2 = int((3*math.pi/2) / step_size)
    print(y_prime_solutionlist[step2], y_prime_solutionlist[step2+1], y_prime_solutionlist[step2+2], y_prime_solutionlist[step2+3], y_prime_solutionlist[step2+4])

    #with pytest.raises(ValueError):
    #    y_prime_solutionlist[step1]
    #with pytest.raises(ValueError):
    #    y_prime_solutionlist[step2]
    #with pytest.raises(ValueError):
    #    y_prime_solutionlist[step2+1]

    #print(step, step+1, step-1)
    #print(step_size)
    #print(y_prime_solutionlist[step])
    #print(y_prime_solutionlist[step + 1])
    #print(y_prime_solutionlist[step - 1])
