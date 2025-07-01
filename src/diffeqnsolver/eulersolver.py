from .solver import Solver


class EulerSolver(Solver):
    def __init__(self, func):
        super().__init__(func)

    def solve(self, x_0: float, y_0: float, x_1: float, num_steps: int = 100):
        self.iterations = [
            (x_0, y_0, self.f(x_0, y_0))
        ]

        x_i = x_0
        y_i = y_0
        step = (x_1-x_0)/num_steps
        for _ in range(num_steps):
            x_i += step
            y_i += step * self.iterations[-1][2]
            self.iterations.append((x_i, y_i, self.f(x_i, y_i)))
