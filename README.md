## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Rationale

- **2.1** What refactoring signs (code smells) suggest this refactoring?
  - Ans: Middle Man
- **2.2** What design principle suggests this refactoring? Why?
  - Ans: Single Responsible Principle(SRP) Because `Movie` should manage movie details,while `Rental` handles 
    pricing logic.This keeps both classes focused and simple.








## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

