import abc

import matplotlib.pyplot as plt


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

    def visualize(self, title: str, function: str):
        """
        Visualizes the results of the solved differential equation

        Args:
            title: string
                Name of the method used
            function: string
                definition of the f(x,y) function used for labelling
        """

        # Function Values:
        x_vals, y_vals, y_prime_vals = zip(*self.iterations)

        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label="y(x)")
        plt.plot(x_vals, y_prime_vals, label="y'(x) = " + function)
        plt.xlabel("x")
        plt.ylabel("Values")
        plt.title("Solution to differential equation using " + title + " Method")
        plt.legend()
        plt.grid(True)
        plt.show()

        print("Plots produced")