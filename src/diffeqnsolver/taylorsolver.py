from .solver import Solver
import math

def derivative(f, a:float, h:float = 1e-05):
    """
    Computes the derivative of a function using the central numerical
    method of differentiation. 

    Args:
        f: function
            Function to be differentiated
        a:float
            Point around which to find the derivative of the function.
        h:float
            Step size around the point of differentiation, a.
            (Default: 1e-05)
    """

    return (f(a+h) - f(a-h)) / (2*h)

def nthDerivative(f, a:float, n:int, h:float = 1e-05):
    """
    Computes the nth derivative of a function using the central numerical
    method of differentiation.

    Args:
        f:function to be differentiated
        a:float
            Point around which to find the derivative of the function.
        n:int
            Order of derivative.
        h:float
            Step size around the point of differentiation, a.
            (Default: 1e-05)
    """
    if n <= 0:
        raise NotImplementedError("Please use a positive order, n.")
    if n == 1:
        return derivative(f, a)
    return ( nthDerivative(f, a+h, n-1) - nthDerivative(f, a-h, n-1) ) / (2*h)


class TaylorSolver(Solver):
    def __init__(self, func):
        super().__init__(func)

    def solve(self, x_0: float, y_0: float, x_n: float, num_steps: int = 100, order: int = 3):
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
            order: int
                Highest order term kept in the Taylor Series expansion.
                (Default: 3)
        """
        if order == 1:
            raise NotImplementedError("""Order of 1 is just the Euler method.
                                      Please use that solver instead!""")
        elif order <= 0:
            raise NotImplementedError("Please input a positive order.")

        self.iterations = [(x_0, y_0, self.f(x_0, y_0))]

        x_i = x_0
        y_i = y_0
        step = (x_n-x_0)/num_steps

        for _ in range(num_steps):
            x_i += step

            Tn = self.iterations[-1][2]
            for i in range(2,order+1):
                Tn += math.pow(step, i-1)/(math.factorial(i)) * nthDerivative(f=self.f, a=x_i, n=i-1)
    
            y_i += step * Tn

            if abs(y_i) > self.inf_threshold:
                raise ValueError(f"Function is diverging near {x_i}")
            self.iterations.append((x_i, y_i, Tn))
