import abc
import numpy as np


class Solver(abc.ABC):
    def __init__(self, func):
        # Eqn to solve (expects a lambda function)
        #  f(x,y) = y'(x)
        self.f = func

        # stores the iterative solutions of the form (x, y(x), y'(x))
        self.iterations: list[tuple] = []

        # infinity threshold
        self.inf_threshold = 1e10

    @abc.abstractmethod
    def solve(self):
        pass

    def visualize(self, title: str):
        """
        Visualizes the results of the solved differential equation

        Args: 
            title: string 
                Name of the method used
            x : array
            y : array
        """

        # Function Values: 
        x = self.iterations[:,0]
        y = self.iterations[:,1]
        z = self.iterations[:, -1]

        plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(projection = '3d') # For graphing f(x,y) = z
        plt.plot(x, y, z)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title("Solution to differential equation using " + title + " Method")
        plt.grid(True)
        plt.show()

        print("Plots produced")

