from .solver import Solver
import math

class TaylorSolver(Solver):
    def __init__(self, func):
        super().__init__(func)

    def solve(self, x_0: float, y_0: float, x_n: float, num_steps: int = 100,derivatives=[]):
        """
        Implements the Taylor method to solve functions of the form y'(x) = f(x,y)
        for y(x). Numerical approximations are made for y(x) for x in the range
        [x_0, x_n] and are stored in the class's `iterations` variable as a list
        of tuples. The tuples are in the form of (x, y(x), y'(x)).

        Args:
            x_0: float
                Initial x value.
            y_0: float
                Initial y value, equivalent to y(x_0).
            x_n: float
                Final x value. Numerical approximations of y(x) are made in the
                range [x_0, x_n].
            num_steps: int
                Number of subintervals in x.
                (Default: 100)
            derivatives: array
                Implicit derivates of the function, given by the user. Must be
                in order i.e. first derivative has 0 index in array, 2nd
                derivative has 1 index, etc. Expects derivatives as a function
                of x and y. 
        """
        if len(derivatives) == 0:
            raise NotImplementedError("""Without derivatives, the Taylor method
            converges to the Euler method. Please use that solver instead!""")

        self.iterations = [(x_0, y_0, self.f(x_0, y_0))]

        x_i = x_0
        y_i = y_0
        step = (x_n-x_0)/num_steps

        for _ in range(num_steps):
            yp_i = Tn = self.f(x_i, y_i)
            for i in range(len(derivatives)):
                Tn += math.pow(step, i+1)/(math.factorial(i+2)) * derivatives[i](x_i,y_i)
    
            x_i += step

            y_i += step * Tn

            if abs(y_i) > self.inf_threshold:
                raise ValueError(f"Function is diverging near {x_i}")
            if abs(yp_i) > self.inf_threshold:
                raise ValueError(f"Derivative is diverging near {x_i}")
            self.iterations.append((x_i, y_i, yp_i))
