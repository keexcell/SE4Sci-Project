import abc

class Solver(abc.ABC):
    def __init__(self, func):
        # Eqn to solve
        self.f = func

        self.coefficients = []
        self.solution = lambda: None

    @abc.abstractmethod
    def solve(self):
        pass

    def visualize(self, title: str):
        pass

