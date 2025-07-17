# SE4Sci-Project: ODE Solvers

Our project aimed to create an ordinary differential equation (ODE) solver with two different numerical methods: the Euler method and the Taylor method.
This solver uses object-oriented programming to create a solver class with an Euler child class and Taylor child class. Both have a separate `solve()` method.
Their parent class also implements a `visualize()` method for plotting the results. Tests were run on first-order ODEs that do have analytical solutions,
making sure that the solver output matches the expected solution at every step within a given tolerance.
