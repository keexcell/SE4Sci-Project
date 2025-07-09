from diffeqnsolver import Solver, EulerSolver
import math
import abc

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

def angle_maker(step, angle_length = 2*math.pi, step_num = 100):
    step_size = angle_length / step_num
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


def test_twovar_trig():
    '''
    Now trying 2 variables, still simpler: f(x,y) = y'(x) = y*tan(x)
    Expect the answer to match y(x) = 1/cos(x)
    x_0 = 0 means y(x_0) = y_0 = 1, go a full period to 2pi
    Each step will be about 0.0628 rad
    '''

    y_prime = EulerSolver(lambda x, y : y*math.tan(x))
    y_prime.solve(0.0, 1.0, 2*math.pi)
    y_prime_solutionlist = y_prime.iterations

    angle_at_step35 = angle_maker(35)
    angle_at_step52 = angle_maker(52)
    angle_at_step71 = angle_maker(71)

    assert check_tuple_close(y_prime_solutionlist[0], (0.0, 1.0, 0.0))
    assert check_tuple_close(y_prime_solutionlist[-1], (2*math.pi, 1.0, 0.0))
    assert check_tuple_close(y_prime_solutionlist[35], (angle_at_step35, 1/math.cos(angle_at_step35), math.tan(angle_at_step35)/math.cos(angle_at_step35)))
    assert check_tuple_close(y_prime_solutionlist[52], (angle_at_step52, 1/math.cos(angle_at_step52), math.cos(angle_at_step52)/math.cos(angle_at_step52)))
    assert check_tuple_close(y_prime_solutionlist[71], (angle_at_step71, 1/math.cos(angle_at_step71), math.cos(angle_at_step71)/math.cos(angle_at_step71)))

    assert check_tuple_far(y_prime_solutionlist[0], (angle_at_step52, 1/math.cos(angle_at_step52), math.cos(angle_at_step52)/math.cos(angle_at_step52)))

    #there's cases where cos = 0 so y = 1/0 and there will be an error. let's figure out what happens there
    step_size = 2*math.pi / 100
    step = int((math.pi/2) / step_size)
    print(y_prime_solutionlist[step])
    print(y_prime_solutionlist[step + 1])
    print(y_prime_solutionlist[step - 1])
