from .solver import Solver


class EulerSolver(Solver):
    def __init__(self, func):
        super().__init__(func)

    def solve(self, x_0: float, y_0: float, x_n: float, num_steps: int = 100):
        """
        Implements the Euler method to solve functions of the form y'(x) = f(x,y)
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
                Number of iterations to perform within the given range.
                (Default: 100)
        """
        self.iterations = [
            (x_0, y_0, self.f(x_0, y_0))
        ]

        x_i = x_0
        y_i = y_0
        step = (x_n-x_0)/num_steps
        for _ in range(num_steps):
            x_i += step
            y_i += step * self.iterations[-1][2]
            yp_i = self.f(x_i, y_i)
            if abs(y_i) > self.inf_threshold:
                raise ValueError(f"Function is diverging near {x_i}")
            if abs(yp_i) > self.inf_threshold:
                raise ValueError(f"Derivative is diverging near {x_i}")
            self.iterations.append((x_i, y_i, yp_i))
