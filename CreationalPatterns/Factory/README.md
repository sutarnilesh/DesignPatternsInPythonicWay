
Creating an object is one of the best ways to track state, and provide methods to describe it's behaviour/process.

# Rather than defining each object manually, why not programmatically?

## In short, Factory is an object that can create objects without the use of a constructor.

*In long* a Factory is a function, method or a subroutine that can return objects that are considered to be 'new'.


## Why not use constructors?
We all are aware that constructors depend heavily on class inheritance. When you make a new object, it exists somewhere
in a template or tree of inherited classes and this is very rigid, fixed design environment.

A factory can create a new object out of any class. It avoids creating any new classes, and new properties can be
assigned to base class using functions or if statements.

### In fact:
*a factory method returns (new) objects.*

For more reference [Factory Design Pattern](https://codeburst.io/what-is-a-factory-design-pattern-d3315ccc912b)