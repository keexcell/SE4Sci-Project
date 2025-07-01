import abc

class Solver(abc.ABC):
    def __init__(self, func):
        self.coefficients = []

    @abc.abstractmethod
    def solve(self):
        pass

    def visualize(self, title: str):
        pass

