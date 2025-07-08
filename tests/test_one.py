from diffeqnsolver import EulerSolver
import math

def tuple_checker(tuple1, tuple2):
	for i in range(len(tuple1)):
		if not math.isclose(tuple1[i], tuple2[i]):
     			return False  
		else:
  			return True

def simple_trig():
	'''
	Just a simple f(x,y) = y'(x) = cos(x) 
	Expect the answer to match y(x) = sin(x)
	x_0 = 0 means y(x_0) = y_0 = 0, go a full period to 2pi
	Each step will be about 0.0628 rad
	'''

	y_prime = EulerSolver(lambda x : math.cos(x))
	y_prime.solve(0.0, 0.0, 2*math.pi)
	y_prime_solutionlist = y_prime.iterations()
	assert tuple_checker(y_prime_solutionlist[0], (0.0, 0.0, 1.0))
	assert tuple_checker(y_prime_solutionlist[-1], (2*math.pi, 0.0, 1.0))
