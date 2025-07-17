# SE4Sci-Project: ODE Solvers

Our project aimed to create an ordinary differential equation (ODE) solver with two different numerical methods: the Euler method and the Taylor method.
This solver uses object-oriented programming to create a solver class with an Euler child class and Taylor child class. Both have a separate `solve()` method.
Their parent class also implements a `visualize()` method for plotting the results. Tests were run on first-order ODEs that do have analytical solutions,
making sure that the solver output matches the expected solution at every step within a given tolerance.

We split the responsibilities of the project among the group and worked with separate branches for a cleaner workflow. Pull requests were made once various
steps were completed to bring the main branch up-to-date with our progress. Kayleigh handled implementing tests for accuracy and expected errors to help with
test-driven development. Justin handled the Euler method and basic package structure. Taylor handled the Taylor method and changes to tests when necessary.
Kyla handled the visualization step embedded in the base class to view the numerical solution `y(x)` and its input derivative `y'=f(x,y)`.
