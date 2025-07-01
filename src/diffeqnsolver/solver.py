import abc


class Solver(abc.ABC):
    def __init__(self, func):
        # Eqn to solve (expects a lambda function)
        #  f(x,y) = y'(x)
        self.f = func

        # stores the iterative solutions of the form (x, y(x), y'(x))
        self.iterations: list[tuple] = []

    @abc.abstractmethod
    def solve(self):
        pass

    def visualize(self, title: str):
        pass

